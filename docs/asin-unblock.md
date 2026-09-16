# ASIN Unblock Kit — swap search links for deep links

## Why /dp/ beats /s?k=
Every link pointing at `https://www.amazon.com/s?k=...` dumps the reader into a
generic Amazon results page where they can buy anything -- or nothing. A deep
`/dp/<ASIN>` link lands them on the exact product we reviewed, which converts
far better. Source: Romanoff growth proposal ("search links convert worse --
swap picks to /dp/ ASINs"). We have 175 unique search queries across the site;
converting even the top picks is the last blocker on this revenue item.

## The 10-minute lookup (Pablo)
1. Open a search link from any page, or just visit
   `https://www.amazon.com/s?k=<search_query>` on the pick you want.
2. On the product page for the correct item, copy the 10-char ID from the
   address bar: `https://www.amazon.com/dp/<ASIN>`.
3. Paste it into the `asin` column of `scripts/asins.csv` next to the matching
   `search_query` row. If a product has no clean ASIN, leave the cell empty.
   Never guess an ASIN -- a wrong one 404s and kills the commission.

## Ship it
```bash
python3 scripts/verify-asins.py          # dry run: previews swaps, edits nothing
python3 scripts/verify-asins.py --apply  # ships the verified swaps
```
The script validates each ASIN (10 chars, starts A-Z), flags empty/invalid
rows, keeps `tag=tradelift-20`, and outputs final link counts. Human approval
happens between the two commands.