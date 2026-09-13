# TradeLift — Progress Tracker

**Last updated:** Sunday, September 13, 2026 (7:20 PM EDT) — FORMSPREE CAPTURE LIVE, email capture fully working

## Status: 🟢 PRODUCTION LIVE + EMAIL CAPTURE WIRED — remotes synced @ `4ab4c06`

Live site: https://pablo63leiva-alt.github.io/tradelift/ (CI auto-deploys on push to `pages/main`). Repo/URL renamed from `blue-collar-hustle-hub` → `tradelift` 2026-09-13.
**Email capture is now REAL (was placeholder):** Newsletter → Formspree `xqpkvyjg`, Quiz career-roadmap capture → Formspree `xzebljww`. Both live-tested `{"ok":true}`. Newsletter double-submit + false-success bugs fixed; quiz already clean (full 2-pass subagent review).

## Milestones

### Done & Shipped — FORMSPREE WIRE (committed `4ab4c06`, deployed, remotes synced)
- [x] Live Formspree IDs in js/main.js (Newsletter `xqpkvyjg`) + js/quiz.js (Quiz `xzebljww`) — replaces `f/YOURID` placeholder
- [x] Rogers Pass 1 + Romanoff Pass 2: wiring verified; both caught pre-existing newsletter bugs → fixed (res.ok guard + Enter-key double-submit, ×2 handlers)
- [x] Deploy success (Actions run 34788992007); verified live JS serves real IDs, all pages 200
- [ ] Formspree account is on a disposable inbox → migrate to real email ASAP (keeps leads + dashboard access)

### Done & Shipped — WAVE 6 (committed `ab3325f`, deployed to production, remotes synced)
- [x] `blog/apprentice-wages-by-year.html` — cross-trade year-by-year table (electrician, plumber, HVAC, welder, carpenter, elevator installer), targets "apprentice wages by year"
- [x] `blog/hvac-apprenticeship-requirements.html` — 2026 checklist, EPA 608, union vs non-union, 5-step apply process, targets "HVAC apprenticeship requirements"
- [x] blog.html: 2 new cards + 2 BlogPosting JSON-LD entries (now 12 total posts)
- [x] Sitemap: 19 URLs (7 main + 12 posts), idempotent ×2
- [x] Re-verified: JS ×3 OK, 20 HTML clean/0 dup IDs, titles ≤60, FAQ parity, salary data site-consistent, internal links resolve

### Done & Shipped — WAVE 5 (committed `303c52b`, deployed to production, remotes synced)
- [x] `blog/hvac-apprentice-salary.html` — "HVAC apprentice salary" year-by-year (targets long-tail)
- [x] `blog/plumber-apprentice-salary.html` — "plumber apprentice salary" year-by-year
- [x] `blog/best-electrician-tools-for-beginners.html` — FIRST affiliate post, 22 amazon `tag=tradelift-20` links + FTC disclosure
- [x] blog.html: 10 cards + 10 BlogPosting JSON-LD; sitemap 17 URLs, idempotent ×2
- [x] Rogers Pass 1 + Romanoff Pass 2 (single gate): 1 Critical + 3 Minor + 3 Minor found → all fixed by Shuri (plumber salary parity $56K-$74K, HVAC year-3 $20, plumber year-4 $22-$32, budget math $158-$297, openings 36,700) + funnel wiring (+tools.html links in salary posts)
- [x] Re-verified: JS ×4 OK, 18 HTML clean/0 dup IDs, 22 affiliate tags, salary bands in-range
- [x] **AUTH QUIRK FOUND & FIXED:** codespace env `GITHUB_TOKEN` shadows OAuth → plain `git push` 403; documented working push command in AGENTS.md + memory

### Done & Shipped — WAVE 4 (committed `4ba3e1b`, deployed to production, remotes synced)
- [x] Blog post: `blog/is-trade-school-worth-it.html` — targets "is trade school worth it"
- [x] Full Twitter/X card metadata across all posts (twitter:card, title, description, image)
- [x] PWA + PDF path repairs (sw.js, manifest.json)
- [x] All dual-QA fixes from prior waves consolidated and deployed
- [x] Baseline re-verified 2026-09-11 8AM EDT: JS ×3 OK, CSS braces 206/64/48, 17 HTML clean / 0 dup IDs, sitemap idempotent 14 URLs, 200 OK on key pages

### Done & Shipped (published to production earlier)
- [x] Project structure scaffolded
- [x] Homepage (index.html), Trades explorer (trades.html, 12 trades + filters), Getting Started (getting-started.html), Resources (resources.html)
- [x] CSS dark industrial theme, JS interactivity (js/main.js)
- [x] GitHub Actions deployment workflow (.github/workflows/deploy.yml) with `enablement: true`
- [x] Missing assets: hero-trades.svg, og-image.png (1200x630), logo.png (512x512)
- [x] Meta/JSON-LD URLs → real Pages domain
- [x] Production repo created (pablo63leiva-alt/blue-collar-hustle-hub, non-fork) + Pages enabled via PAT
- [x] Deploy workflow passed; verified live (all pages HTTP 200) — pre-wave build

### Done in the 2026-09-10 PUBLISH WAVE (committed `1950774`, NOT yet pushed)
- [x] Blog: blog.html + 2 SEO posts (how-to-become-an-electrician, trade-school-vs-college) w/ Article + FAQPage schema
- [x] Quiz: quiz.html + js/quiz.js + css/quiz.css — 10-question "Which Trade Is For You?" (all 12 trades reachable)
- [x] Lead capture: Formspree newsletter + exit modal w/ honeypot, validation, mailto fallback
- [x] Integration: uniform nav (Home/Trades/Getting Started/Resources/Blog/Quiz), hero quiz CTA, blog teaser, callouts, canonicals on all pages, sitemap 8 URLs
- [x] QA: Rogers (Pass 1, 20 findings) + Romanoff (Pass 2, independent functional, 7 findings) — all fixed by Shuri (21 fixes) and re-verified
- [x] NEWS: Fury Wave 2 — quiz-results email capture funnel (docs/conversion-funnel.md) built, verified, awaiting review-pass before bundling into deploy
- [x] **RESUME SESSION (2026-09-10 ~7 PM):** Rogers Pass-1 funnel findings applied by Shuri (M1 email label, m1-m5 dead code/guard/print/doc). Rogers Pass-1 on Lang's Wave-3 share cards (0 critical, 2 major, 7 minor) → fixes by Shuri (preview via canvas, iOS failure fallback + SVG new-tab, no leak, async disabled state, fixed px fonts, escaping, aria, doc typo). Romanoff Pass 2 (independent, jsdom 36-assertion harness) → 2 major (double-submit-in-flight, fetch HTTP-status ignored), 1 minor (stale label restore), 2 info (aria-hidden-on-visible, capture analytics beacon) → all fixed by Shuri. Final re-verify green (node --check ×3, CSS braces 63/63 + 206/206 + 48/48, html.parser clean ×9 pages, 0 dup IDs). Committed. **Deploy still blocked on creds.**
- [x] **CONTENT WAVE 2 (2026-09-10 ~11 PM):** 2 SEO posts by Hawkeye (blog/best-trades-for-16-year-olds.html targets "trades for 16 year olds", blog/is-welding-a-good-career.html targets "is welding a good career"/"welder salary 2026") + blog.html integration (2 cards + JSON-LD BlogPosting → 4 posts, title/meta/og tightened ≤60 chars, meta desc 134) + sitemap generator blogPosts +2 (now 10 URLs, idempotent). Rogers Pass-1 (0 crit, 0 major, 6 minor) + Romanoff Pass-2 (real Chromium render + click-through, 0 crit/0 major, 2 minor SEO-length) → all minors fixed by Shuri (FAQ summary↔JSON-LD verbatim parity ×8, OSHA-10 age hedge ×2, welding CTA wording, titles ≤60, related-card copy, AGENTS.md/SESSION-MEMORY count sync 8→10 URLs). PM re-verify: html.parser clean ×3, sitemap identical ×2 (10 URLs). Committed. **Deploy still blocked on creds.**

### RESOLVED
- [x] **Push to production (`git push pages main`)** — unblocked 2026-09-11 via `gh auth login --web` device flow (OAuth token scopes: gist/read:org/repo, stored ~/.config/gh/hosts.yml chmod 600, git credential helper wired). NOTE: env GITHUB_TOKEN is still metadata-only; use `env -u GITHUB_TOKEN gh ...` for API calls. Editing workflow files later requires `workflow` scope.

### Done — LANG OG CARDS (2026-09-11, NOT committed)
- [x] `scripts/generate-og-cards.js` — reusable/idempotent Node script (Playwright headless Chromium, `require('playwright')` with `/tmp/opencode/qa2` fallback): parses 12 `TRADES` verbatim from `js/quiz.js`, renders self-contained 1200x630 HTML per trade (`deviceScaleFactor:1`, clip 1200x630), in-script per-trade PASS assertion (name + salary in DOM), writes `img/og-<slug>.png`.
- [x] Generated 12 PNGs (all `1200x630`, >370KB, byte-identical on re-run — sha256 match 12/12). Buyer-side wiring: `blog/is-welding-a-good-career.html` og:image → og-welder.png, `blog/how-to-become-an-electrician.html` og:image → og-electrician.png (only those 2 lines changed; html.parser clean both).
- [x] Docs: "OG cards" section appended to `docs/social-sharing.md` (usage + 12-file table).
- [x] Deploy still blocked on creds; nothing committed/pushed.

### Done — SHURI CONSOLIDATED QA FIX LIST (2026-09-11, Rogers Pass 1 + Romanoff Pass 2, NOT committed)
- [x] Electrician salary parity: non-union journey-level $26-$34/hr/$52K-$68K → $30-$38/hr/$60K-$76K; year-4 range unified to "$20-$32/hr ($25-$32/hr union)" in FAQ schema + visible (electrician-apprentice-salary.html).
- [x] Electrician apprenticeship length normalized "4 year" → "4–5 year" (trades.html, widget/quiz.html, highest-paying table; body phrase).
- [x] Construction Manager entry "Experience + degree" → "Experience + promotions" (trades.html, widget/quiz.html).
- [x] JSON-LD Article/Twitter images → trade cards (how-to + apprentice-salary → og-electrician.png, is-welding → og-welder.png; blog.html BlogPosting images synced).
- [x] FAQPage ↔ visible verbatim parity fixed in all 6 posts (schema answers/names edited or visible updated; incl. "$0 while paying you", welding Q4 framing, how-to Q5/Q6 names).
- [x] Titles ≤60 / desc ≤160 all 6 posts; ONE canonical headline per post propagated verbatim across title/og/twitter/Article/BlogPosting/blog-card h3 + related cards.
- [x] Footer Blog link added (index/trades/getting-started/resources/quiz/tools).
- [x] "radiation therapists" → "commercial airline pilots" (highest-paying post).
- [x] tools.html: WebPage JSON-LD added, CTA demoted to btn-outline, affiliate placeholder comment removed.
- [x] Re-verified: html.parser clean 16/16, JSON-LD 0 errors, 0 dup IDs, all internal hrefs resolve, headline/card consistency green, FAQ verbatim green, node --check ×3 OK, CSS braces balanced (206/63/48), sitemap idempotent 13 URLs.

## The Fork/PAT History (why production is a separate repo)
- GitHub refused Pages on the original fork. Fresh non-fork repo created; Pages enabled via API + classic PAT (`repo`+`workflow`); deploy workflow succeeds on push.
- PAT is a credential of the user; do not persist its value anywhere in this repo.

## Notes
- Production pushes → `pages` remote (tradelift). Deploy is automatic on push to `main` there.
- The 12:19 PM EDT snapshot (2026-09-10) of project/memory/instructions lives in `docs/SESSION-MEMORY.md`.

## Optional / Future Work
- Fix deploy blocker (credentials) — top priority.
- Review + deploy Fury funnel wave.
- Affiliate pages (tools per trade), more blog posts (2-4/mo), quiz share images (12), widget embed for schools, Meta retargeting pixel, Google Search Console verification.
- Revenue playbooks live in docs/monetization.md + docs/conversion-funnel.md.