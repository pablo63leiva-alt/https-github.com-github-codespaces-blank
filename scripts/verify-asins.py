#!/usr/bin/env python3
"""verify-asins.py — ASIN unblock kit (read-only by default).

Scans every *.html file under the repo root for Amazon href URLs, splits them
into /s?k= (search) and /dp/ (product) buckets, and matches them against an
optional scripts/asins.csv keyed by the decoded search query.

Search links (e.g. https://www.amazon.com/s?k=Klein%20MM400%20multimeter&tag=...)
convert worse than deep links. This tool shows exactly which /s?k= links are
ready to become https://www.amazon.com/dp/<ASIN>?tag=tradelift-20 -- but it
NEVER invents an ASIN. It only ever works from ASINs a human pasted into
asins.csv, and it will not let tag=tradelift-20 get lost.

Usage:
    python3 scripts/verify-asins.py            # dry run (default, read-only)
    python3 scripts/verify-asins.py --apply    # applies validated swaps only
"""

import argparse
import csv
import os
import re
import sys
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO_ROOT, "scripts", "asins.csv")
TAG = "tag=tradelift-20"

# Amazon search links look like https://www.amazon.com/s?k=<query>
SEARCH_RE = re.compile(r"^https://www\.amazon\.com/s\?k=")
# /dp/ links look like https://www.amazon.com/<slug>/dp/<ASIN>
DP_RE = re.compile(r"^(https://www\.amazon\.com/)([^/]*/)?dp/([A-Z][A-Z0-9]{9})(\?[^\"']*)?")
HREF_RE = re.compile(r"""href\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
# A valid ASIN is exactly 10 chars: first char uppercase A-Z, rest alphanumeric.
ASIN_RE = re.compile(r"^[A-Z][A-Z0-9]{9}$")
# The href attribute value in HTML may contain &amp; instead of &.
HTML_AMP_RE = re.compile(r"&amp;")


def find_html_files(root):
    """Yield every *.html under root, skipping hidden dirs and .git."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if name.endswith(".html"):
                yield os.path.join(dirpath, name)


def decode_query(value):
    """HTML-unescape then URL-decode an s?k= value into plain search text."""
    value = HTML_AMP_RE.sub("&", value)
    return urllib.parse.unquote_plus(value)


def index_html_files(html_files):
    """Return (all_links, search_by_query, dp_links).

    all_links:          list of (html_file, raw_href) for every Amazon href.
    search_by_query:    dict decoded_query -> list of (html_file, raw_href).
    dp_links:           list of (html_file, raw_href) for /dp/ Amazon hrefs.
    """
    all_links = []
    search_by_query = {}
    dp_links = []
    for path in html_files:
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        for match in HREF_RE.finditer(text):
            href = match.group(1)
            if not href.startswith("https://www.amazon.com/"):
                continue
            all_links.append((path, href))
            if "s?k=" in href:
                query = href.split("s?k=", 1)[1].split("&", 1)[0]
                query = decode_query(query)
                search_by_query.setdefault(query, []).append((path, href))
            elif "/dp/" in href and DP_RE.match(href):
                dp_links.append((path, href))
    return all_links, search_by_query, dp_links


def read_asins_csv(path):
    """Read scripts/asins.csv; return (rows, warnings).

    Row is a dict with search_query, title, asin. Broken lines and comment
    lines are skipped with a warning. Empty/malformed stuff is the caller's
    job to flag -- we never drop a row silently past here.
    """
    rows = []
    warnings = []
    if not os.path.exists(path):
        return rows, ["asins.csv not found at " + path + " (nothing to map yet)"]
    # utf-8-sig tolerates a BOM if someone edits the file in Excel.
    with open(path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        expected = {"search_query", "title", "asin"}
        missing = expected - set(reader.fieldnames or [])
        if missing:
            warnings.append("asins.csv missing column(s): " + ", ".join(sorted(missing)))
            return rows, warnings
        for lineno, raw in enumerate(reader, start=2):
            if not raw or not raw.get("search_query"):
                continue
            rows.append(
                {
                    "search_query": raw["search_query"].strip(),
                    "title": (raw.get("title") or "").strip(),
                    "asin": (raw.get("asin") or "").strip(),
                    "lineno": lineno,
                }
            )
    return rows, warnings


def valid_asin(asin):
    """True only for a well-formed ASIN: 10 chars, A-Z first, alnum rest."""
    return bool(asin) and bool(ASIN_RE.fullmatch(asin))


def replacements_for(rows, search_by_query):
    """Pair CSV rows to site links.

    Returns dict decoded_query -> {"row": row, "links": [(file, href), ...]}
    only for rows whose query actually appears in the site AND whose ASIN is
    valid. Site-detected but CSV-less queries are reported separately.
    """
    mapped = {}
    for row in rows:
        query = decode_query(row["search_query"])
        if not valid_asin(row["asin"]):
            continue
        if query not in search_by_query:
            continue
        mapped[query] = {"row": row, "links": search_by_query[query]}
    return mapped


def minimal_url(asin):
    """The exact minimal deep link, tag preserved."""
    return "https://www.amazon.com/dp/%s?%s" % (asin, TAG)


def apply_substitutions(mapped, search_by_query):
    """Replace s?k= hrefs with /dp/ hrefs in place. Returns (changed, total)."""
    files_to_patch = {}
    for query, info in mapped.items():
        for path, href in info["links"]:
            files_to_patch.setdefault(path, []).append((href, minimal_url(info["row"]["asin"])))
    changed_files = 0
    applied = 0
    for path, swaps in sorted(files_to_patch.items()):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        new_text = text
        for old_href, new_href in swaps:
            if new_text.count(source_href(old_href)) and source_href(old_href) != new_href:
                new_text = new_text.replace(source_href(old_href), new_href)
                applied += 1
        if new_text != text:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
            changed_files += 1
    return changed_files, applied


def source_href(raw_href):
    """Canonical form of a href for replacement -- keep the raw entity form."""
    return raw_href


def main():
    parser = argparse.ArgumentParser(description="Verify /s?k= -> /dp/ ASIN swaps (read-only unless --apply).")
    parser.add_argument(
        "--dry-run", action="store_true", default=True,
        help="Only preview switches; never touch files. (default ON)",
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Apply substitutions already validated by scripts/asins.csv.",
    )
    args = parser.parse_args()
    apply_mode = bool(args.apply)
    if apply_mode:
        args.dry_run = False

    html_files = list(find_html_files(REPO_ROOT))
    all_links, search_by_query, dp_links = index_html_files(html_files)
    rows, warnings = read_asins_csv(CSV_PATH)

    total_search_links = sum(len(v) for v in search_by_query.values())
    unique_queries = len(search_by_query)
    mapped = replacements_for(rows, search_by_query)

    valid_asins = [r for r in rows if valid_asin(r["asin"])]
    invalid_asins = [r for r in rows if not valid_asin(r["asin"]) and r["asin"] != ""]
    empty_asins = [r for r in rows if r["asin"] == ""]

    print("=" * 72)
    print("ASIN UNBLOCK KIT — /s?k= -> /dp/ verification")
    print("=" * 72)
    print("Repo scanned : %s" % REPO_ROOT)
    print("HTML files   : %d" % len(html_files))
    print("Amazon hrefs : %d total (%d search/%s links, %d /dp/ links)"
          % (len(all_links), total_search_links, "s?k=", len(dp_links)))
    print("Unique s?k= queries: %d" % unique_queries)

    print()
    print("asins.csv: %d row(s)" % len(rows))
    for w in warnings:
        print("  WARN: " + w)
    print("  ASINs valid   : %d" % len(valid_asins))
    print("  ASINs empty   : %d (still need a human lookup)" % len(empty_asins))
    flagged = [r for r in invalid_asins if r["asin"] != ""]
    if flagged:
        print("  ASINs invalid : %d" % len(flagged))
        for r in flagged:
            print("    line %d: %r (%s) -> INVALID ASIN %r ignored" % (r["lineno"], r["title"], r["search_query"], r["asin"]))

    print()
    print("PREVIEW — swaps this kit WOULD make (nothing edited yet):")
    ready_links = 0
    for query, info in sorted(mapped.items()):
        before_total = len(info["links"])
        asin = info["row"]["asin"]
        ready_links += before_total
        sample_file, sample_href = info["links"][0]
        print("  [%2d x] %s" % (before_total, info["row"]["title"]))
        print("          search_query : %s" % query)
        print("          before       : %s" % sample_href)
        print("          after        : %s" % minimal_url(asin))
        if before_total > 1:
            print("          (+%d more occurrences, including %s)"
                  % (before_total - 1, info["links"][1][1]))
    if not mapped:
        print("  (none — add valid ASINs to scripts/asins.csv first)")

    still_needed = unique_queries - len(mapped)
    print()
    print("REPORT:")
    print("  Unique s?k= queries        : %d" % unique_queries)
    print("  Queries mapped to an ASIN  : %d" % len(mapped))
    print("  Queries still need an ASIN : %d" % max(still_needed, 0))
    print("  /dp/ links already present : %d" % len(dp_links))
    print("  Invalid ASINs flagged      : %d" % len(flagged))
    print("  Search links ready to swap : %d" % ready_links)

    if apply_mode:
        changed_files, applied = apply_substitutions(mapped, search_by_query)
        print()
        print("APPLY RESULT:")
        print("  Files patched : %d" % changed_files)
        print("  Links swapped : %d" % applied)
        remaining = total_search_links - applied
        print("  s?k= links left: %d (all remaining need an ASIN in asins.csv)" % max(remaining, 0))
        print("FINAL: %d /dp/ links now live; run without --apply to re-verify." % applied)
    else:
        print()
        print("FINAL: %d search links are ready to swap -- review the preview," % ready_links)
        print("       get each ASIN human-verified, then run:")
        print("         python3 scripts/verify-asins.py --apply")
        print("       A second pass (agent-applied, human-approved) completes the job.")


if __name__ == "__main__":
    main()