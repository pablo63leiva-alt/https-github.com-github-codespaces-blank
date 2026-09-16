# TradeLift — Progress Tracker

**Last updated:** Wednesday, September 16, 2026 (11:40 AM EDT session) — DEPLOYED: 4 new PPE affiliate gear posts (32 posts total, 43 sitemap, live) + Fury PR/ASIN docs committed.

# TWO TRACKS (as of 2026-09-16)

## Track B — TableText (working name) — RESTAURANT SMS LOYALTY AUTOMATION
## Status: 🟡 MVP-KIT BUILT (consent/launch/pilot docs) — waiting on Pablo account + name
> **2026-09-16 RESUME session:** 3 parallel deliverables landed + QA'd. Nakia → `docs/tabletext-consent-and-privacy.md` (11-element consent line, privacy policy skeleton, logging spec, 12-item pre-launch checklist). Okoye → `docs/tabletext-launch-kit.md` (3 QR-tent variants, landing wireframe+copy, 4 blast templates <160ch, 12-mo calendar, $49/$99 sales page). Ramonda → `docs/tabletext-pilot-outreach.md` + `docs/tabletext-pilot-leads.csv` + `docs/pilot-feedback.md` (20-lead sheet, email/call/walk-in scripts, pilot agreement, feedback loop). QA: 3 MUST FIX + 7 minor all fixed (consent brand prefix, 2-text cap unified, 9PM quiet-window, print-vs-ship, Monday timing, consumer copy).
- [ ] **NEXT (Pablo):** pick name/GTM/stack + create SimpleTexting or Twilio account → then T'Challa/Shuri² scaffolds MVP. Ramonda pilot outreach ready to fire from leads sheet.

## Track A — TradeLift (@ tradelift.surge.sh) — PRIMARY MONEY ENGINE
## Status: 🟢 PRODUCTION LIVE — 32 blog posts, 43-URL sitemap, email capture live

> Deployed today (09-16 11:40 AM): `d213f58` — 4 PPE affiliate gear posts (hard hats, safety glasses, tool bags, work gloves; 49 `tag=tradelift-20` links), blog.html 32 cards/BlogPosting, sitemap 43, QA fixes (tool-bag title parity, gloves salary bands, blog.html indent), newsletter wire-ins on tool-bags + safety-glasses, Fury PR docs (HARO/Reddit kit, state-of-trade draft, ASIN unblock kit + verify script). Live-verified 200 on all new posts + sitemap 43.

### Done & Shipped — 2026-09-16 11:40 AM SESSION (committed `d213f58`, deployed, origin synced)
- [x] **Hawkeye: 4 NEW PPE affiliate posts (32 total)** — `blog/best-hard-hats-for-trade-workers.html` (15 links), `blog/best-safety-glasses-for-trades.html` (10), `blog/best-tool-bags-for-apprentices.html` (12), `blog/best-work-gloves-for-construction.html` (12). blog.html 32 cards + 32 BlogPosting; sitemap → **43 URLs** (idempotent ×2).
- [x] **Dual QA:** Rogers Pass 1 — PASS (0 crit/major; minors: gloves "(2026)" in title-not-H1 → fixed; gloves salary band $18-25/$50-80K → canonical $15-25/$45-80K). Romanoff Pass 2 — 2 CRITICAL fixed (tool-bags title/metadata mismatch → unified "Best Tool Bags for Apprentices"; tool-bags missing from sitemap → regenerated), 3 MAJOR (tool-bags + safety-glasses missing newsletter sections → added matching hard-hats/gloves pattern; blog.html indent; /s?k= vs /dp/ → documented via ASIN unblock kit, blocked on Pablo).
- [x] **Other work in commit:** `docs/haro-reddit-kit.md` (Fury), `docs/state-of-trade-careers-2026.md` (Fury draft), `docs/asin-unblock.md` + `scripts/verify-asins.py` + `scripts/asins.csv` (Fury/Stark ASIN kit), `docs/tabletext-mvp-build.md` (T'Challa). outreach-strategy.md copy honesty fixes (5,000+ claims → "thousands").
- [ ] **NEXT (Jarvis):** more affiliate gear posts (electrician/plumber/HVAC gloves/tool brands), salary-parity reconciliation pass (plumber $55-75K vs $56-74K, electrician $60-80K vs $60-80K+), mid-article quiz CTAs (Shuri).
- [ ] **NEXT (Pablo):** run `scripts/verify-asins.py` after pasting ASINs into `scripts/asins.csv` (10-min lookup per docs/asin-unblock.md); Gumroad publish; Buttondown; UTI/Lincoln pitches; GSC submit; PA-API key.

### Done & Shipped — 2026-09-15 PM SESSION #2 (committed `9a2fee9`, deployed, origin synced)
- [x] **Hawkeye: 4 NEW posts (28 total)** — `blog/best-work-boots-for-apprentices.html` + `blog/best-welding-helmets-for-beginners.html` (gear affiliates, 7 Amazon links each, `tag=tradelift-20`), `blog/how-to-pay-for-trade-school.html` + `blog/what-to-expect-first-year-trade-school.html` (trade-school education guides, 0 affiliates). blog.html 28 cards + 28 BlogPosting; sitemap → **39 URLs** (idempotent ×2).
- [x] **Dual QA (subagents):** Rogers Pass 1 — 1 major fixed (welder band → $45K-$70K+) + 2 minors (read-time, nav). Romanoff Pass 2 — **PASS** (44/44 links, 16/16 salaries, 14/14 affiliate tags, 0 fake ASINs, edu posts clean). 1 minor (helmet price $250→$300) fixed. **All live 200, sitemap 39 live.**
- [x] **CRO `def214b`:** mid-article crosslinks — helmets→welder starter kit, how-to-pay→tradeschools hub (Romanoff growth proposals).

## Track B — TableText (working name) — RESTAURANT SMS LOYALTY AUTOMATION (NEW 2026-09-15)
## Status: 🔵 RESEARCHED + SQUAD STOOD UP by 12:55 PM save — brief at `docs/vibe-smart-loyalty.md`
- [x] **Market research (subagent, live-verified):** white space confirmed — nothing purpose-built for QR→form→CRM→SMS→blasts for independent restaurants. Textdrip precedent (indie $20-75/mo works). Positioning recommended: $49/mo Table Lead Kit + $99/mo DFY wedge; "works with ANY POS"; flat price, no per-text math.
- [x] **Technical research (subagent, live-verified):** SMS providers compared (Twilio $0.012-15/msg full price; SimpleTexting no-code fastest; Textlocal SHUT DOWN), 10DLC/TCPA compliance captured (11-element consent disclaimer verbatim; $500-1500/msg fines), MVP stack = Tally+Carrd+SimpleTexting (~$60-90/mo) or Twilio+Supabase+Vercel (~$180-280).
- [x] **New squad stood up:** Manager **T'Challa** + 6 subagents (Shuri², Namor, Nakia, Okoye, M'Baku, Ramonda) — full roles in brief §4. Runs parallel to TradeLift lane.
- [ ] **NEXT:** Pablo picks name/GTM/stack → T'Challa scaffolds no-code MVP (needs SimpleTexting/Twilio account under Pablo's email) → Nakia writes consent line → Okoye QR tent + blast templates → M'Baku QA → Ramonda pilot outreach.

---

## Track A Detail — Prior milestones (Keep)

Live site: https://tradelift.surge.sh/ (Surge.sh; deploy = `bash scripts/deploy-surge.sh`). GitHub Pages disabled 2026-09-13; the `pages` remote repo is an archived code mirror only — never push there (dead workflow would re-enable Pages; editing workflows needs `workflow` scope). Dev copy: `origin`.
**Email capture is now REAL (was placeholder):** Newsletter → Formspree `xqpkvyjg`, Quiz career-roadmap capture → Formspree `xzebljww`. Both live-tested `{"ok":true}`. Newsletter double-submit + false-success bugs fixed; quiz already clean (full 2-pass subagent review).

## Milestones

### Done & Shipped — SESSION 2026-09-15 8AM: REVENUE SPRINT #2 (committed `a122220`, deployed, live-verified)
- [x] **NEW PAGE `tradeschools.html`** — "Trade Schools & Training" lead-gen hub (~2200 words): trade-school vs apprenticeship table, 12-trade training-path grid (salaries == quiz.js/trades.html canonicals), top US trade schools summary w/ official links + FTC disclosure, quiz + newsletter funnel integration. High-CPA education play. **Deployed + live 200.**
- [x] **NEW PAGE `privacy.html`** — AdSense-ready Privacy Policy: Formspree/localStorage data handling, future ads/analytics, CCPA/GDPR rights, COPPA, affiliate disclosure, contact placeholder. Canonical surge, footer in all pages. **Deployed + live 200.**
- [x] **Wiring:** `Trade Schools` nav + footer link on all 7 main pages + privacy footer; quiz email-capture success now has "Compare top trade schools" CTA; sitemap 32 URLs (idempotent ×2); robots refs sitemap.
- [x] **SEO fix:** BlogPosting JSON-LD now carries `description` on all 22 entries (parsed from each post's meta description; JSON valid, desc ≤160).
- [x] **New revenue stream:** `resources.html` — "Student Money-Savers" section: Amazon Prime Student + Audible free-trial links (?tag=tradelift-20) + full Amazon Associates disclosure.
- [x] **Bug fixes (js/main.js):** exit-modal focus-trap idempotent (dataset guard) + live focusable recompute (no stale-capture); removed dead `beforeunload` handler.
- [x] **Dual QA:** Romanoff PASS (0 crit/major; fixed: Diesel/Automotive naming parity, privacy footer gap). Rogers PASS (fixed: privacy footer active-state, footer link order, focus-trap live recompute, sitemap regen to 32).
- [x] **Live-verified:** tradeschools/privacy 200, all key pages 200, sitemap 32 live, protected files still 404.
- [ ] **NEXT (Pablo):** Gumroad account + publish $12 guide (storefront-launch-kit.md ready); Buttondown free tier + migrate email; UTI/Lincoln partner pitches (CPL); real contact email replaces hello@ placeholder; migrate Formspree off disposable inbox.
- [ ] **NEXT (Jarvis):** premium-CTA once Gumroad live; 44 /s?k= affiliate links → /dp/ ASINs; GSC submit; email-sequence automation.

### Done & Shipped — SESSION 2026-09-14: CAREER GUIDE PDF + 2 AFFILIATE POSTS + SOCIAL/DOCS (squad)
- [x] **Stark:** `scripts/generate_career_guide.py` → `assets/careers.guide` — 15-page branded Trade Career Fit Guide (12 trades + 90-day plan + resources), **salary bands fixed to match quiz.js/trades.html canonicals** (was spec-derived) + verified `Salary bands verified: OK`
- [x] **Career guide wired into funnel:** `quiz.html` post-email "Download your FREE Career Fit Guide" button; `js/quiz.js` `showCareerGuideDownload()` after email capture; `js/main.js` exit-modal copy now pitches the guide
- [x] **Fury:** `blog/best-plumbing-tools-for-apprentices.html` — 20 Amazon `tag=tradelift-20` links, FTC disclosure, "Our Top Pick" badges, wired into blog.html grid + BlogPosting JSON-LD
- [x] **Wiring fix:** `blog/best-welding-equipment-for-beginners.html` added to blog.html grid + BlogPosting array (was unwired)
- [x] **Banner:** `docs/social-media-strategy.md` — 90-day calendar, 6 content pillars, hashtags, KPIs (5300 followers, ≥5% eng, 12% email capture)
- [x] **Vision:** technical SEO audit (see section above) — 0 remaining issues
- [ ] **GAP — 3 Hawkeye posts on disk but NOT wired into blog.html:** `how-to-become-a-plumber-step-by-step`, `highest-paying-trade-careers-2026`, `best-trade-schools-in-america` → need blog cards + BlogPosting JSON-LD + sitemap regen
- [ ] **GAP — Shuri CRO tasks pending** (exit-modal upgrade, benefit microcopy, trust signals) — cancelled by capacity
- [ ] **GAP — `docs/outreach-strategy.md` NOT persisted** (agent claimed created; file absent) → recreate
- [ ] **GAP — NOT deployed:** this session's work is on `origin` only; surge deploy pending (`bash scripts/deploy-surge.sh`)
- [ ] **GAP — Formspree still on disposable inbox** → migrate to real email

### Done & Shipped — TECHNICAL SEO AUDIT & FIXES (2026-09-14, Vision)
- [x] Sitemap: regenerated idempotent ×2 → 22 URLs (7 main + 15 posts incl. new `best-welding-equipment-for-beginners.html`); all files exist, lastmod 2026-09-13/14, no 404s; robots.txt sitemap ref OK
- [x] **Fixed:** `trades.html` — added `id` anchor on all 12 trade-card `<article>`s + replaced 12 `href="#"` "Learn More" CTAs → `href="#<trade>"`. Resolves pre-existing logged issue: widget/quiz.html + blog CTAs link `trades.html#<id>`, which previously had no matching anchors
- [x] **Fixed:** meta descriptions >160 chars on `apprentice-wages-by-year`, `hvac-apprenticeship-requirements`, `best-welding-equipment-for-beginners`
- [x] **Fixed:** `badge.html` missing OG/Twitter (added full set + robots index); `widget/quiz.html` missing OG/Twitter (added, og:url → canonical quiz.html); `widget/demo.html` missing canonical → added canonical + `noindex` (dev demo)
- [x] **Fixed:** mobile tap targets — `.filter-btn` (8/20→12/22px), `.social-link` (40→44px), `.nav-toggle` hit area (8→10/12px)
- [x] Verified: all 25 HTML well-formed; 0 dup meta/clean JSON-LD (Article/FAQPage parity 5-6 Qs each); FAQ schema ↔ visible `<details>` match on all 15 posts; BlogPosting JSON-LD + blog.html cards consistent (new post needs card + BlogPosting entry — content task)
- [x] Noted (left intact by design): footer social `href="#"` placeholders (no real profile URLs); og-*.png ~370KB social-card images (not page-rendered; page images all <5KB)
- [x] JS ×3 `node --check` OK; CSS braces balanced; no horizontal-scroll risk (body `overflow-x:hidden`, fluid max-widths)

### Done & Shipped — WAVE 1 REVENUE SPRINT (2026-09-13, deployed, on `origin`)
- [x] 2 new SEO posts → 14 total: `blog/carpenter-apprentice-salary.html` ("carpenter apprentice salary") + `blog/how-to-become-a-welder.html` ("how to become a welder"); blog.html 14 cards + 14 BlogPosting; sitemap now 21 URLs, executable glob
- [x] 12 per-trade Career Roadmap PDFs (`scripts/generate-roadmaps.py` → `assets/roadmaps/<slug>-roadmap.pdf`) — site-consistent salary bands; served **extensionless** on surge (blocks .pdf); quiz email-capture success now offers the matching roadmap download (HEAD-guarded, null-safe)
- [x] `tag=tradelift-20` verified on ALL 94 affiliate links (tools.html ×72 + tools post ×22); Amazon Associate ID confirmed by Pablo
- [x] Merch pipeline: `merch/designs/` 12×3000px PNG+SVG (electrician, welder, hvac, plumber, …) + `merch/launch-kit.md` listings + `merch/README.md` (Etsy/Printful steps) + `merch/generate-merch.js`
- [x] `docs/REVENUE-OPS.md` — $50K-by-Dec-22 ops plan: pillars, month-by-month table (Sep→Dec), ONLY-PABLO list, Jarvis-autonomy list, 3 scenarios, KPI dashboard
- [x] Dual QA PASS (Rogers structural + Romanoff functional): 0 blocking; non-blocking notes → widget/quiz.html result-CTAs anchor-ids don't exist on trades.html (pre-existing, logged)
- [x] DEPLOYED + verified (14 posts 200, roadmaps 200, careers.guide 200, sitemap 21, canonical surge, quiz CTA live)
- [ ] Next (Pablo action): GSC verify → submit sitemap; Amazon Associates tax/payment interview; Etsy/Printful + payout accounts by Nov 1; migrate Formspree off disposable inbox

### Done & Shipped — HOST MOVE TO SURGE (2026-09-13, committed on `origin`)
- [x] Repo rename → `tradelift` gave short github.io URL, then **full move OFF GitHub Pages**: live site = https://tradelift.surge.sh (no more github.io — confirmed 404)
- [x] All 200+ absolute URLs → surge base (canonical/og/twitter/json-ld/sitemap/sw/manifest/robots); God-style path-safety verified by dual QA (Rogers clean, Romanoff live-verified)
- [x] Surge quirks solved: `.pdf` blocked → lead-magnet served as `assets/careers.guide` (octet-stream download, `download="trade-lift-5-trades.pdf"`); PWA manifest rooted at `/`; `scripts/deploy-surge.sh` reproducible deploy
- [x] CI converted to health checks (no Pages deploy); github.io Pages disabled; `pages` remote archived
- [x] eu.org: `tradelift.eu.org` app prepped (contact PL1771-FREE validated link saved, no captcha) — approval ~2-6 wks, optional long-term custom domain

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
- Revenue playbooks live in docs/monetization.md + docs/conversion-funnel.md.- [2026-09-14] Stark: generated the 12 quiz-funnel Career Roadmap PDFs (`scripts/generate-roadmaps.py` → `assets/roadmaps/<slug>-roadmap.pdf`). Salary bands = exact trades.html/quiz.js figures, IDENTICAL for all 12 (no contradiction possible with site). Blog-cited BLS medians for electrician/plumber/welder/HVAC/carpenter/pipefitter; 6 trades (auto/diesel/mason/roofer/ironworker/CM) marked "assumed — no dedicated post yet" in `assets/roadmaps/README.md`. Idempotent (invariant=1 → byte-identical reruns, md5-verified). Built-in verify: 12 PDFs exist, >10KB, 2 pages, pypdf text extract, quiz.js name/salary sync. Not deployed (per mission).
