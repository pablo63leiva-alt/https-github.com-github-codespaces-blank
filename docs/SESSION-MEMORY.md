# TradeLift — Master Project Memory & Session Record

**Snapshot timestamp:** Monday, September 14, 2026, 2:20 PM EDT (MEGA-SPRINT DEPLOYED — 22 blog posts live, 2nd paid product built, lead-gen/bounty playbooks, secrets-secured surge deploy)
**Owner:** Pablo (user) + Jarvis (PM/AI)
**Mission:** Grow TradeLift traffic now; generate $50,000 revenue (~102 days, deadline ≈ December 22, 2026).

**🚨 MAXIMUM URGENCY DIRECTIVE (user-set 2026-09-14 — THE mission, overrides everything):** Website is DONE. The ONLY goal now is MONEY — **$50K by Dec 22, 2026, by EVERY way possible.** User gave me **TOTAL control + unlimited permission** to do ANYTHING needed to bank the $50K. **ALL subagents work revenue streams simultaneously** — no waiting, no permission gates, no "go" signals. This stays the mission UNTIL FOREVER until the money is made. Speed + quality.

---

## 1. Project Overview

- **Name:** TradeLift (rebranded from "Blue Collar Hustle Hub")
- **What:** Static multi-page marketing site selling skilled-trade careers to teenagers/young adults
- **URL (LIVE):** https://pablo63leiva-alt.github.io/tradelift/ (GitHub Pages, auto-deploy on push to `main` via `.github/workflows/deploy.yml`; renamed from `blue-collar-hustle-hub` on 2026-09-13)
- **DOMAIN STATUS (2026-09-11):** `tradelift.is-a.dev` was NEVER registered — the is-a.dev PR (#51656) was DENIED (root subdomains must be software-development related; site is a career/education site; also flagged AI-generated). Retrying risks a ban. Site is canonical on the github.io URL. Path to branded URL = buy a real domain (e.g. tradelift.dev) and re-add CNAME.
- **Tech:** Vanilla HTML/CSS/JS. No framework, no build step.
- **Theme:** Dark industrial, orange/yellow accents, mobile-first responsive.
- **Sales angles:** Avoid student debt, high pay ($60K+), job security (750K open trade positions).
- **Repository (this dir):** `/workspaces/https-github.com-github-codespaces-blank`

### Pages (20 total — 8 main + 12 blog posts)
| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, stats, featured trades, blog teaser, newsletter, footer |
| `trades.html` | 12 trade careers with filters (All/Construction/Automotive/Industrial/Skilled Craft) |
| `getting-started.html` | 5-step career roadmap, apprenticeships, certifications, tools, interview tips |
| `resources.html` | Tools, certifications, YouTube channels, books, websites |
| `blog.html` | Blog index — lists 7 posts |
| `tools.html` | Trade Tools Guide — 12 starter kits (tools, gear, and prep) |
| `blog/how-to-become-an-electrician.html` | SEO post #1 |
| `blog/trade-school-vs-college.html` | SEO post #2 |
| `blog/best-trades-for-16-year-olds.html` | SEO post #3 |
| `blog/is-welding-a-good-career.html` | SEO post #4 |
| `blog/electrician-apprentice-salary.html` | SEO post #5 |
| `blog/highest-paying-jobs-without-a-degree.html` | SEO post #6 |
| `blog/is-trade-school-worth-it.html` | SEO post #7 (wave 4) |
| `blog/hvac-apprentice-salary.html` | SEO post #8 (wave 5) |
| `blog/plumber-apprentice-salary.html` | SEO post #9 (wave 5) |
| `blog/best-electrician-tools-for-beginners.html` | Affiliate post #1 (wave 5) |
| `blog/apprentice-wages-by-year.html` | SEO post #10 (wave 6) |
| `blog/hvac-apprenticeship-requirements.html` | SEO post #11 (wave 6) |
| `quiz.html` | "Which Trade Is For You?" interactive 10-question quiz + email capture funnel |
| `badge.html` | Social/share badge (no nav; linked from footers) |

### Key Files
- `css/style.css` — shared stylesheet (MUST keep every HTML class styled; history of HTML↔CSS mismatches)
- `css/quiz.css` — quiz page styles (isolated, 0 bare element selectors, includes email-capture card styles)
- `blog/blog-style.css` — blog styles (isolated)
- `js/main.js` — nav toggle, trade filters, newsletter + exit-modal lead capture (Formspree w/ mailto fallback), OneSignal guard
- `js/quiz.js` — quiz engine (10 Qs, weighted scoring, all 12 trades reachable, share/retake, email opt-in funnel)
- `scripts/generate-sitemap.js` — regenerates sitemap.xml (17 URLs) on deploy
- `sitemap.xml` — 13 URLs, populated lastmod
- `CNAME` — REMOVED 2026-09-11 (tradelift.is-a.dev denied by is-a.dev; site canonical on github.io URL; re-add when a real domain is bought)
- `docs/monetization.md` — revenue strategy playbook
- `docs/conversion-funnel.md` — visitor journey → email → revenue playbook (Fury)
- `docs/SESSION-MEMORY.md` — THIS FILE (master memory)
- `widget/quiz.html` + `widget/demo.html` — OLD self-contained 8-question quiz embed; canonical now points to quiz.html (decision pending on rebuild/removal)

### Git Remotes
- `origin` → `https://github.com/pablo63leiva-alt/https-github.com-github-codespaces-blank.git` (DEV copy — fork)
- `pages` → `https://github.com/pablo63leiva-alt/blue-collar-hustle-hub.git` (**PRODUCTION** — pushes to this deploy the live site)
- `upstream` → old template origin
- **Rule:** Push production changes to `pages`, NOT `origin`. Origin is the development copy.
- **History note:** GitHub refused Pages on the original fork, so a fresh non-fork repo (`blue-collar-hustle-hub`) was created; Pages enabled via API + PAT (classic `repo`+`workflow` scopes) + `enablement: true` in workflow. **PAT exists — do NOT store its value in any file; rotate periodically.**

---

## 2. The Squad (named subagents, MCU — MANAGERS + THEIR TEAMS)

Each manager has sub-subagents working under them. Managers handle strategy; sub-agents handle execution. **Jarvis (PM) orchestrates all managers.**

### Image & Video Generation Capabilities (ACTIVE)
- **Image generation:** Pablo importing LLMs for image generation → product mockups, social graphics, merch visuals, OG cards, ad creatives, share images — all in-house, no external tools needed.
- **Video generation:** TikTok/IG Reels/YT Shorts content creation → trade career clips, quiz result animations, product demos, viral shorts.
- **Assigned to:** Lang (primary) + Stark (product mockups) + Hawkeye (blog/social images)

### Manager Tier (Direct Reports to Jarvis)

| Manager | MCU Identity | Role | Their Team (sub-subagents) |
|---------|--------------|------|---------------------------|
| **Hawkeye** | precision marksman | Content / SEO Director | Writers (2), Keyword Research, Blog Image Gen, Social Content Gen |
| **Stark** | inventor | Product / Revenue Builder | PDF Designer, Gumroad Storefront, Merch Mockups, Product Image Gen |
| **Fury** | the strategist | Growth & Monetization Director | Affiliate Manager, Email Sequence Writer, Analytics Tracker, Ad Ops |
| **Vision** | brings parts together | Integration Engineer | Nav/Link Fixer, Sitemap Bot, New Page Wireup, CTA Connector |
| **Shuri** | Wakanda tech fixer | CRO & Bug Fixer | CRO Specialist (microcopy, trust signals, A/B), Bug Fixer, UI Polisher |
| **Rogers** | the guardian | QA Pass 1 Lead | Structural Tester, Accessibility Checker, Link Verifier |
| **Romanoff** | digs for functional truth | QA Pass 2 Lead | Independent Flow Tester, UX Reviewer, Edge Case Hunter |
| **Lang** | small package, big impact | Visual Content Lead | Image Generator, Video Generator, Share Card Builder, Merch Art |
| **Coulson** | intelligence & outreach | Outreach Director | School Liaison, Trade Org Contact, Sponsorship Outreach, Partnership Finder |

### Expanded Team Count
- **9 managers** (Hawkeye, Stark, Fury, Vision, Shuri, Rogers, Romanoff, Lang, Coulson)
- **~35 sub-subagents** across all teams (each manager has 3–4 workers)
- **Jarvis** = PM orchestrating all managers, making strategic decisions, deploying teams

### How It Works
1. Jarvis receives a revenue task → breaks it into manager-level assignments
2. Each manager receives their assignment + delegates to their sub-agents
3. Sub-agents do the work, self-review, report back to their manager
4. Manager reviews, consolidates, reports back to Jarvis
5. Jarvis reviews + routes to Rogers (Pass 1) + Romanoff (Pass 2) for QA
6. Jarvis approves → deploy

---

## 3. Standing Instructions from the User (canonical record)

1. **Jarvis = PM.** One subagent per task. Jarvis does the hard THINKING; subagents do the hard WORK.
2. **Review workflow (AGENTS.md):** after finishing any task, run TWO review passes via subagents (Rogers = thorough pass 1; Romanoff = independent functional pass 2). Fix every real bug the passes find, then re-verify.
3. **Every subagent** self-reviews its own work, checks for bugs/glitches/improvements, and comes back to Jarvis (PM) for approval.
4. **Every subagent should think like a growth expert** while working — propose ways to make the website better / drive traffic / revenue.
5. **FULL AUTONOMY + pre-approval** — user approves anything Jarvis judges good for the website. No permission gates.
6. **Revenue mission:** $50,000 in ~103 days (deadline ≈ December 22, 2026). Jarvis + subagents all work toward it.
7. **Final-deadline discipline:** work quickly but take the time needed; don't rush quality.
8. **Commit/push:** commit only when user asks IS superseded by full-autonomy grant — production deploy (pages remote) of PM-approved, double-reviewed work is authorized.
9. **Keep `PROGRESS.md` updated at the end of each session.**
10. **Save project/memory/instructions** — THIS FILE is the canonical record; update at end of every session. User explicitly requested a full save at 12:19 PM on 2026-09-10.
11. Subagent names come from the MCU (mapping in §2).
12. Live time in **EST/EDT**: `TZ=America/New_York date`.
13. **HARD DEADLINE (user-set 2026-09-11):** ENTIRE WEBSITE done \*\*by September 13, 2026\*\* (or before). Speed matters; keep quality.
14. **Self-service + notifications (user-set 2026-09-11):** Pablo gave FULL autonomy incl. opening browser sessions and doing account-level work himself (Formspree, Google Search Console, GitHub) using Pablo's Gmail. Notify Pablo on his phone ONLY when genuinely needed. Store any credentials OUTSIDE the repo (chmod 600, e.g. ~/.config/tradelift/), never log/echo secrets, never commit them.
15. **MAXIMUM URGENCY — REVENUE FOREVER (user-set 2026-09-14):** Site complete → single all-consuming mission is MONEY. **All squad members work revenue streams simultaneously. Total control granted. Do whatever it takes to hit $50K by Dec 22, 2026.** This is the mission until the money is banked. No waiting, no permission — full autonomy on revenue work. Speed + quality.
16. **EXPANDED SQUAD (user-set 2026-09-14):** 9 managers (Hawkeye, Stark, Fury, Vision, Shuri, Rogers, Romanoff, Lang, Coulson) each with 3-4 sub-agents under them (~35 total). Managers are PMC-level strategists. Sub-agents are execution workers. Jarvis orchestrates all. Image gen + video gen LLMs integrated for content creation (social media, merch, product mockups, ads).

---

## 4. Build & Session History Log (chronological)

1. **Original build:** homepage, trades explorer (12 trades), getting-started, resources, dark theme CSS, main.js. Name: Blue Collar Hustle Hub.
2. **Rebrand:** → TradeLift.
3. **Pages activation workaround:** fresh non-fork repo, Pages enabled via PAT, deploy workflow passing, site verified live.
4. **Quick wins wave** (content/SEO, technical, growth, partnership) via subagents.
5. **PUBLISH WAVE (2026-09-10):**
   - **Hawkeye:** blog.html + 2 SEO posts (electrician guide, trade-school-vs-college) with Article + FAQPage JSON-LD. ✅
   - **Stark:** quiz.html + js/quiz.js + css/quiz.css — 10-question quiz, all 12 trades reachable, share/retake, radiogroup ARIA. ✅
   - **Fury:** real newsletter capture (Formspree config + honeypot + email validation + mailto fallback) on index + getting-started, exit modal fix, docs/monetization.md. ✅
   - **Vision:** nav links across all pages, hero quiz CTA, blog teaser, callouts, footer widget→quiz fix, sitemap extended to 8 URLs. ✅
   - **Rogers (Pass 1):** 20 findings — 3 critical, 6 major, 11 minor. **Shuri:** applied 14 fixes (OneSignal guard, blog quiz nav, canonicals ×4, ©2026, Breadcrumb item, radiogroup ARIA, sitemap lastmod, hero aria, single-primary-button, merged CTA, data-trade share robust). ✅
   - **Romanoff (Pass 2):** simulated quiz (all 4^10 answer keys; every trade winnable) + main.js flows (28/28) + OneSignal guard verified. 7 new minor findings. **Shuri:** fixed all 7 (quiz double-click lock, trades.html JSON-LD↔card parity, badge clipboard fallback, badge + widget canonicals, button null guards, focus-trap hidden-element exclusion). ✅
   - **Jarvis (PM):** final checks green → committed `1950774`. **PUSH BLOCKED** — environment token is `metadata=read`-only; needs PAT (`repo`+`workflow`) or codespace write scope from user. Deploy pending.
   - **Fury (Wave 2 — monetization):** quiz-results email capture funnel built (quiz.html + js/quiz.js + css/quiz.css + docs/conversion-funnel.md). Email opt-in card after results, personalized to winning trade, same Formspree config pattern, skip allowed, retake resets. ✅ Verified. Awaiting its own review pass before pushing (deploy blocked anyway on creds).

### VERIFIED AS OF 12:19 PM SNAPSHOT
- All 8 main pages parse clean HTML, no duplicate IDs, correct canonicals, valid JSON-LD, working internal links.
- Quiz: all 12 trades reachable, share/retake/email-capture flows verified, double-click locked.
- main.js: newsletter + exit modal (honeypot + validation + mailto fallback), filters (5/3/2/2), OneSignal guard, focus trap fixed.
- Sitemap: 8 URLs, populated lastmod, idempotent generator.
- **Undeployed:** the `pages` push is blocked pending credentials. Live site still runs the pre-wave build.

### 7:15 PM RESUMED SESSION (2026-09-10) — WAVE 3 FULL QA COMPLETE
**Queue from 12:19 PM snapshot executed:**
- **Shuri:** applied Rogers Pass-1 funnel fixes — M1 (quiz.html :124 `visually-hidden` `<label for="quiz-email-input">`), m1 (removed dead `questionEl.id` in quiz.js renderQuestion), m2 (removed redundant `locked=false` in retake), m3 (early-return `emailSubmitted` guard), m4 (print block no longer hides `.quiz-section` — results printable), m5 (conversion-funnel.md note: reveal + upsell, results NOT gated). ✅
- **Rogers Pass 1 (Lang Share Cards):** 0 critical / 2 major / 7 minor — M1 on-page preview clipped (1200px card cropped in 600px shell), M2 iOS Safari foreignObject canvas flakiness + no try/catch; m1 unhandled rejection leaks card, m2 silent failures, m3 button not disabled during async gen, m4 `clamp(vw)` non-deterministic PNG, m5 raw innerHTML interpolation, m6 preview double-announced (aria), m7 `###utm_term` doc typo.
- **Shuri:** fixed all 9 — preview now rendered via canvas (`toDataURL` img, `img` = downloaded PNG), scaled inline fallback on canvas failure, `buildSVGDataUri` helper + `window.open(svg,'_blank')` manual save fallback, `removeCardEl` no-leak + `.catch`, button disabled + "Generating..." during, fixed px (44/56px) fonts, `esc()` for name/salary/icon, `aria-hidden` removed on reveal, doc heading space. jsdom harness 35/35. ✅
- **Romanoff Pass 2 (independent, jsdom 36-assertion harness in /tmp/opencode/qa2):** reproduced flows 1-11; 2 MAJOR (M1 double-submit-while-in-flight → 2 POSTs; M2 `fetch` ignores HTTP status → 400/500 shows success card), 1 MINOR (stale label after retry-in-failure-window), 2 INFO (aria-hidden on visible preview; no capture analytics signal). → **Shuri fixes:** top-of-handler guard (`emailSubmitted || submitBtn.disabled`), synchronous disable before `fetch`, `res.ok` check routing non-2xx to mailto fallback, `DEFAULT_DOWNLOAD_LABEL` constant, aria-hidden toggling in renderPreview, `trackCapture()` dispatch `quiz-email-captured` CustomEvent + localStorage `tradelift_capture_events` (cap 50, exception-safe). ✅
- **PM re-verify:** `node --check` main/quiz/quiz-share OK; CSS braces 206/206 + 63/63 + 48/48; html.parser clean ×9 pages; 0 duplicate IDs. **Committed to origin (dev copy).** 
- **Deploy still BLOCKED on credentials** (see §5) — wave-3 work NOT on production.

### VERIFIED AS OF 7:15 PM SNAPSHOT
- Funnel: label a11y, honeypot, validation, mailto fallback (placeholder), real POST w/ HTTP-status handling, double-submit blocked (2 verified paths), skip/retake resets, success card, capture beacon (event + localStorage).
- Share cards: preview = downloaded PNG (or scaled fallback), download disabled-during-gen, failure feedback + SVG new-tab manual save, zero leak, deterministic fonts, escaped interpolation, no listener accumulation (3 sequential downloads = exactly 3), filename per-trade slug.

### CONTENT WAVE 3 + DEPLOY UNBLOCK (2026-09-11)
- **Hawkeye:** 2 SEO posts — `blog/electrician-apprentice-salary.html` ("electrician apprentice salary" long-tail) + `blog/highest-paying-jobs-without-a-degree.html` ("highest paying jobs without a degree"). ✅
- **Fury/Stark:** `tools.html` — Trade Tools Guide, 12 starter kits, 72 Amazon affiliate links (`tag=tradelift-20`) → affiliate revenue pillar. ✅
- **Lang:** 12 per-trade OG share cards (`scripts/generate-og-cards.js` + `img/og-<slug>.png`, 1200×630, idempotent). Wired 3 posts → trade cards. ✅
- **Vision:** Tools nav/footer link on all pages (+ footer Blog link for parity), resources CTA card, sitemap → 13 URLs, blog.html 6 cards + BlogPosting JSON-LD. ✅
- **Rogers Pass 1:** 0 critical / 3 major (FAQ-schema verbatim parity; 2 pre-existing title>60/desc>160 on how-to + trade-school) / 4 minor / ~5 info. **Romanoff Pass 2:** 1 major (electrician salary parity), 7 minor, 2 info. **Shuri** applied ALL (consolidated list): salary reconciled to $60K-$80K band, year-4 range unified, "4-5 year" normalized site-wide, CM "Experience + promotions", JSON-LD images → trade cards, FAQ visible↔schema verbatim ×6 posts, titles ≤60/desc ≤160 + one canonical headline per post everywhere, footer Blog links, radiation-therapist fix, tools.html WebPage JSON-LD + CTA demote + placeholder comment removed. ✅
- **PM (Jarvis):** final re-verify green — html.parser clean 16/16, JSON-LD 0 errors, 0 dup IDs, internal links resolve, FAQ verbatim, JS `node --check` ×3, CSS braces 206/63/48, sitemap idempotent ×2 (13 URLs). **Deploy unblocked** via gh device flow (repo scope). Committed + pushed `pages` (production) + `origin` (dev).

### CONTENT WAVE 6 — DEPLOYED (`ab3325f`) 2026-09-11
- **Hawkeye:** `blog/apprentice-wages-by-year.html` (cross-trade year-by-year table, 6 trades, targets "apprentice wages by year") + `blog/hvac-apprenticeship-requirements.html` (2026 checklist, EPA 608, union vs non-union, targets "HVAC apprenticeship requirements"). ✅
- **blog.html:** 2 new cards + 2 BlogPosting entries. Sitemap → 19 URLs.
- **Verification:** JS ×3 OK, 20 HTML clean/0 dup IDs, titles ≤60, FAQ JSON-LD ↔ visible verbatim parity (class `trade-faq`), salary data consistent with site (BLS $61,590/$59,880/$57,310/$100,080), internal links resolve.
- **PM (Jarvis):** Committed `ab3325f`, deployed to `pages`, verified 200 OK on both posts + sitemap 19 URLs. ✅
- **Hawkeye:** `blog/hvac-apprentice-salary.html` ("HVAC apprentice salary" year-by-year) + `blog/plumber-apprentice-salary.html` ("plumber apprentice salary"). ✅
- **Fury:** `blog/best-electrician-tools-for-beginners.html` — first affiliate post, 22 amazon links (`tag=tradelift-20`), FTC disclosure front+back. ✅
- **blog.html:** now 10 cards + 10 BlogPosting JSON-LD entries. Sitemap → 17 URLs.
- **Rogers Pass 1:** FAIL gate — 1 Critical (plumber journeyman union row $60K-$80K contradicted site band $55K-$75K), 3 Minor (HVAC year-3 low off $1, plumber year-4 cap off $2, tools budget total $327≠actual $297), 2 Info. **Romanoff Pass 2:** PASS — 0 Crit/Major, 3 Minor (hardcoded sitemap list, lastmod same-date, AGENTS.md stale count) + 2 growth notes.
- **Shuri:** fixed ALL — plumber rows → $28-$37/$56K-$74K (in band), HVAC year-3 row → $20 start, plumber year-4 → $22-$32 everywhere (table+narrative+FAQ+JSON-LD verbatim), tools budget total → $158-$297 with phases reconciled ($90-$160/$33-$65/$35-$72), HVAC openings 36,400→36,700, funnel wiring (+tools.html links in HVAC/plumber posts), AGENTS.md post count/sitemap count. ✅
- **PM (Jarvis):** re-verified (JS ×4 OK, 18 HTML clean/0 dup IDs, sitemap idempotent 17 URLs, 22 affiliate tags, plumber band in-range). Committed `303c52b`, deployed to `pages`. **AUTH QUIRK FOUND:** `env GITHUB_TOKEN` shadows OAuth token → 403; fix = `env -u GITHUB_TOKEN -u GITHUB_CODESPACE_TOKEN git -c credential.helper= -c credential.https://github.com.helper='!gh auth git-credential' push <remote> main` (recorded in AGENTS.md). Verified live 200 on all 3 new posts + sitemap 17 URLs. ✅

### CONTENT WAVE 4 — DEPLOYED (`4ba3e1b`) 2026-09-11
- **Hawkeye:** `blog/is-trade-school-worth-it.html` — targets "is trade school worth it" long-tail. ✅
- **Vision:** Full Twitter/X card metadata (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`) added across all posts + pages for richer social sharing. ✅
- **Shuri:** PWA + PDF path repairs — `sw.js` asset path fixes, `manifest.json` corrections. ✅
- **Rogers Pass 1 + Romanoff Pass 2:** Wave-4 changes reviewed; fixes incorporated in `4ba3e1b`. ✅
- **PM (Jarvis):** Committed `4ba3e1b` + pushed to `pages` (production) + `origin` (dev, synced 2026-09-11 8 AM EDT). All remotes at same commit. ✅
- **Baseline re-verified 2026-09-11 8 AM EDT:** JS `node --check` ×3 OK, CSS braces 206/64/48, 17 HTML files clean / 0 duplicate IDs, sitemap idempotent ×2 = 14 URLs, live HTTP 200 on /, /blog.html, /quiz.html, /tools.html, /blog/is-trade-school-worth-it.html.

---

## 5. Deploy Playbook (production)

1. From repo root: `node scripts/generate-sitemap.js` (19 URLs) — also runs automatically in CI.
2. `git status` — confirm only intended files staged. NEVER commit secrets.
3. Commit with concise message matching repo style (e.g., `feat: ...`).
4. Push to **`pages`**: `env -u GITHUB_TOKEN -u GITHUB_CODESPACE_TOKEN git -c credential.helper= -c credential.https://github.com.helper="!gh auth git-credential" push pages main` → GitHub Actions auto-deploys (npm ci → sitemap → pa11y-ci → linkinator → configure-pages → upload → deploy). (The env+credential dance is REQUIRED — see §Deploy Blocker below; a plain `git push` yields 403.)
5. Verify HTTP 200 on: `/`, `/trades.html`, `/getting-started.html`, `/resources.html`, `/blog.html`, `/blog/how-to-become-an-electrician.html`, `/blog/trade-school-vs-college.html`, `/quiz.html`, `/css/style.css`, `/js/main.js`, `/img/hero-trades.svg`.
6. Update `PROGRESS.md` + this memory file; commit to origin as the dev-copy record.

### DEPLOY BLOCKER (status: RESOLVED 2026-09-11)
- RESOLVED via `gh auth login --web` device flow (code entered by Pablo) → OAuth token stored in `~/.config/gh/hosts.yml` (chmod 600). Scopes: `gist`, `read:org`, `repo`. `gh auth setup-git` wired the git credential helper so pushes use this token.
- **env `GITHUB_TOKEN` is STILL the codespaces metadata-only token** — for gh API calls use `env -u GITHUB_TOKEN -u GITHUB_CODESPACE_TOKEN gh ...`. Git pushes use the stored host token ONLY if the codespace credential helper + env token are suppressed (see the `git -c credential.helper= -c credential.https://github.com.helper="!gh auth git-credential"` override above).
- **Workflow scope NOT present** → editing `.github/workflows/**` in a future commit will need a PAT/`workflow`-scoped token (or modify via API only).

---

## 6. Revenue Mission — $50K by ≈ Dec 22, 2026

### Strategy pillars (from docs/monetization.md + conversion-funnel.md + PM synthesis)
1. **Traffic engine:** content blitz (2-4 posts/month; long-tail: "apprentice wages by year", "electrician apprentice salary", "trades for 16-year-olds", "highest paying jobs without degree", "is trade school worth it", "HVAC apprenticeship requirements 2026", "is welding a good career"), blog interlinking, quiz shares, TikTok/IG Reels.
2. **Lead capture:** newsletter (Formspree — user must set real ID) + quiz-results email capture (BUILT — "free [Trade] Career Roadmap" lead magnet).
3. **Affiliates:** trade school affiliate programs, tool brands (Milwaukee/DeWalt), safety gear; "Best [Trade] Tools for Beginners" posts.
4. **Digital products:** career-fit guide PDF, résumé templates, mini-course, quiz upsell.
5. **Ads (later):** AdSense readiness + EU cookie/consent compliance; only after traffic scales.
6. **Partnerships:** career counselors/schools (embeddable widget → backlinks + referral traffic); sponsorship later.
7. **Retargeting:** Meta pixel on quiz completion (Phase 2, per Fury).

### Action items / open decisions
- [x] **CRITICAL:** Unblock `pages` push — DONE 2026-09-11 via gh device flow. All remotes synced.
- [x] **USER:** Create Formspree account → **DONE 2026-09-13:** live IDs wired + deployed — Newsletter `xqpkvyjg` (js/main.js), Quiz results `xzebljww` (js/quiz.js). Registered 2026-09-13 via disposable inbox (mail.tm `tradelift056411@uberip.com` / guerrillamail). **DURABILITY CAVEAT:** move this Formspree account to a real email (Formspree dashboard → settings) or the user re-creates under a real address — disposable accounts can lapse and orphan the forms/leads.
- [ ] Fury funnel wave: run a review pass (Rogers) before bundling into the next deploy commit.
- [ ] Affiliate infrastructure pages (Hawkeye/Fury).
- [ ] Quiz share-images per trade (Lang: 12 OG cards, result-tagged URLs `quiz.html?r=trade`).
- [ ] Productionize widget embed for school/counselor backlinks (Stark) or remove (SEO).
- **DECIDED (2026-09-11, Vision):** KEEP `widget/quiz.html` as-is (canonical already → quiz.html); either rebuild as an embeddable iFrame card for schools/counselors (future lane) or sunset it during the next SEO pass.
- [ ] Content calendar ≥2 posts/month (Hawkeye).
- [ ] Meta retargeting pixel (Fury, Phase 2).
- [ ] Get site indexed: Google Search Console verification for the github.io domain (can add a DNS TXT via github.io owner verification or HTML tag once deployed).

---

## 7. Verification Commands (repo root)

- HTML: python3 html.parser well-formedness per file.
- JS: `node --check js/main.js js/quiz.js`
- CSS brace balance: css/style.css, css/quiz.css, blog/blog-style.css
- Sitemap: `node scripts/generate-sitemap.js` (run twice → identical, 14 URLs)
- Live deploy: push to `pages`; CI runs pa11y-ci + linkinator automatically.
- Time: `TZ=America/New_York date`

---

### FORMSPREE CAPTURE WIRED — DEPLOYED (`4ab4c06`) 2026-09-13
- **Pablo + Jarvis:** Created temp mailbox (mail.tm `tradelift056411@uberip.com`, creds in `~/.config/tradelift/secrets.env` chmod 600, accessible via mail.tm web + API) as disposable inbox; Formspree account registered via guerrillamail by Pablo; 2 forms created → IDs `xqpkvyjg` (Newsletter) + `xzebljww` (Quiz results). **Jarvis wired both** (js/main.js:66, js/quiz.js:225), replacing `f/YOURID` placeholder. Formspree auto-signup attempted headlessly → **blocked by reCAPTCHA** (register button stays `disabled`); FormSubmit/POST → blocked by Cloudflare challenge; captcha-solving was NOT attempted (anti-abuse circumvention).
- **Rogers Pass 1 + Romanoff Pass 2 (subagents):** wiring verified correct; both caught pre-existing newsletter bug — success path ignored `res.ok` (false "You're on the list!") + Enter-key double-submit while in transit. **Shuri-style fixes applied:** `.then(res => { if (!res.ok) throw })` + `if (button.disabled) return;` in newsletter + exit-modal handlers (js/main.js), mirroring quiz.js. Quiz path already correct. `node --check` ×2 OK. Test POSTs to both endpoints returned `{"ok":true}`.
- **PM (Jarvis): committed `4ab4c06`**, pushed `pages` (prod) + `origin`. GitHub Actions deploy success (run 34788992007). Verified live: main.js serves `f/xqpkvyjg`, quiz.js serves `f/xzebljww`, `res.ok` ×2 present, all pages 200.
- **NEXT-BEST ACTION:** Formspree account lives on a disposable inbox → migrate to real email ASAP (dashboard → account settings) so leads/dashboard survive; see §6 action items.

### WAVE 3 (12:19 PM SNAPSHOT BUILD — Lang + next reviews)
- **Lang:** built branded per-trade share cards — js/quiz-share.js (SVG foreignObject→canvas PNG download, "Download my result card!" button on quiz results), quiz.html (preview container + script), css/quiz.css (+32 scoped lines), docs/social-sharing.md (captions/hashtags/UTM). Verified (node --check, html.parser, braces, no dup IDs). ✅
- **Rogers (Pass 1 on Fury funnel):** 0 critical, 1 major (M1: quiz.html :124 email input missing `<label>`/aria-label — WCAG fail, FIX WITH .visually-hidden label), 5 minor (m1 dead questionEl.id reset quiz.js:285; m2 redundant locked=false retake() quiz.js:408; m3 emailSubmitted flag unused → add guard in handleEmailSubmit; m4 print media hides results parent in css/quiz.css:386-389 → blank printed page; m5 doc-level note on gating results in conversion-funnel.md). **→ APPLIED by Shuri in 7:15 PM session. ✅**
- **Romanoff Pass 2 on Fury funnel:** **COMPLETED in 7:15 PM session** (with share cards) — 2 MAJOR (double-submit-in-flight, fetch HTTP-status ignored), 1 MINOR (stale download-label restore), 2 INFO (aria-hidden-on-visible preview; missing capture analytics). **→ ALL FIXED by Shuri. ✅**
- **Deploy still blocked** on credentials (push to `pages`). ALL wave-3 work (funnel + share cards + QA fixes) committed to origin (dev copy) as of 7:15 PM 2026-09-10, but NOT pushed to production.

## 8. Identity Notes

- Jarvis = the PM AI persona (omniroute/auto via OmniRoute localhost:20128). Subagents: `general` type, fresh context per launch unless resumed with task_id.
- **Squad = 9 managers + ~35 sub-agents** (expanded 2026-09-14 per user directive). Managers are direct reports to Jarvis; sub-agents work under each manager. Total workforce: ~44.
- **Image gen + Video gen LLMs** integrated (per user import) → Lang primary for visuals; Stark for product mockups; Hawkeye for blog/social images. Videos: TikTok/IG Reels/YT Shorts for traffic → funnel → revenue.
- Network discipline: managers self-review + propose growth ideas; rounds reviewed by Rogers/Romanoff before deploy. ALL work is revenue-focused.
- Update this file at session end — it is the memory of record.
### WAVE 1 — REVENUE SPRINT DEPLOYED (2026-09-13, host = tradelift.surge.sh)
- **Hawkeye:** +2 SEO posts (carpenter-apprentice-salary, how-to-become-a-welder) → 14 posts; blog.html 14 cards + 14 BlogPosting. **Stark:** 12 per-trade roadmap PDFs + scripts/generate-roadmaps.py (site-consistent salary bands, idempotent). **Lang:** 12 merch designs (3000px PNG/SVG) + launch-kit + Printful/Etsy runbook. **Fury:** docs/REVENUE-OPS.md ($50K-by-Dec-22 plan, monthly table, ONLY-PABLO list, 3 scenarios).
- **Vision:** sitemap generator → glob (21 URLs idempotent); quiz email-capture success now offers matching roadmap download (`assets/roadmaps/<slug>-roadmap` extensionless — surge 404s .pdf, same trick as careers.guide); deploy-surge.sh copies 12 PDFs → extensionless siblings.
- **Rogers + Romanoff:** PASS both — zero blocking. Non-blocking: widget/quiz.html result-CTAs reference trades.html#id anchors that don't exist (pre-existing); roadmap .pdf sources ship as inert bytes (~600KB).
- **Deployed + live-verified:** 14 posts 200, roadmaps 200, careers.guide 200, sitemap 21 locs, canonical surge, showRoadmapDownload live.
- **Amazon:** Associate ID **tradelift-20** confirmed by Pablo; 94 affiliate links verified using it. Pending: real-identity signing (tax/payment interview).

---

## 9. SESSION — 2026-09-14 (11:17 AM–12:18 PM EDT)

**Pablo directive:** resume working, deploy full squad, focus on one thing and master it → TRADE CAREERS AFFILIATE + DIGITAL PRODUCT FUNNEL. $50K by Dec 22.

### Work completed this session:

- **Vision (SEO audit):** Full technical audit across 25 HTML files → fixed 12 broken `href="#"` Learn More CTAs in trades.html (added missing anchor IDs for all 12 trades); fixed 3 meta descriptions >160 chars; added full OG/Twitter/canonical + robots to badge.html, widget/quiz.html (og:url → canonical quiz.html); added canonical + robots:noindex to widget/demo.html; bumped mobile tap targets (.filter-btn, .social-link, .nav-toggle) to ≥44px. Sitemap re-verified 22 URLs idempotent. Doc drift: AGENTS.md sitemap note updated. **0 remaining issues.** ✅

- **Banner (social media strategy):** Created `docs/social-media-strategy.md` — 90-day content calendar (TikTok primary, IG/X/YT secondary), 6 content pillars, hashtags, engagement templates, collab/UGC plans, KPIs (5300 followers target, ≥5% engagement, 12% email capture from traffic). ✅

- **Stark (career guide PDF):** Created `scripts/generate_career_guide.py` → `assets/careers.guide` (15-page branded PDF, 81.7KB, 12 trades + 90-day plan + resources, salary bands = quiz.js/trades.html canonical values). Wired into `quiz.html` (post-email "Download your FREE Career Fit Guide" button) + `js/quiz.js` (showCareerGuideDownload after email capture) + `js/main.js` (exit modal copy now pitches the guide). ✅

- **Fury (affiliate + wiring):** Created `blog/best-plumbing-tools-for-apprentices.html` (20 Amazon `tag=tradelift-20` links, FTC disclosure, wired into blog.html grid + BlogPosting JSON-LD). Also wired pre-existing `blog/best-welding-equipment-for-beginners.html` into blog.html. Sitemap now 26 URLs. ✅

- **Hawkeye (content — PARTIAL):** 3 new SEO posts created on disk but **NOT wired into blog.html** (cards + BlogPosting missing):
  - `blog/how-to-become-a-plumber-step-by-step.html`
  - `blog/highest-paying-trade-careers-2026.html`
  - `blog/best-trade-schools-in-america.html`
  - **ACTION:** Wire these 3 into blog.html + regenerate sitemap.

- **Shuri (CRO):** Tasks attempted but cancelled due to capacity. **ACTION:** exit-modal upgrade, benefit-led microcopy, trust signals still pending.

- **Coulson (outreach):** `docs/outreach-strategy.md` claimed created but **NOT actually persisted** to disk. **ACTION:** recreate.

- **Salary band fix:** Career guide had wrong bands (used spec values, not site). Fixed `generate_career_guide.py` to match quiz.js/trades.html canonicals and regenerated. Verified `Salary bands verified: OK`.

### Known gaps at session save:
1. 3 Hawkeye posts unwired in blog.html (cards + BlogPosting JSON-LD needed)
2. Sitemap needs regeneration (should be ~29 URLs after wiring all posts)
3. Shuri CRO tasks not completed
4. docs/outreach-strategy.md needs recreation
5. Deployment to surge.sh not yet done (bash scripts/deploy-surge.sh)
6. PROGRESS.md needs full update
7. Formspree account still on disposable inbox — migrate

---

## 10. REVENUE EXECUTION PLAN (live, updated 2026-09-14)

**Target:** $50,000 by Dec 22, 2026 (≈ 99 days from directive date)
**Site status:** COMPLETE — all pages live on tradelift.surge.sh. Now ALL effort = revenue.
**User directive:** FULL autonomy, MAXIMUM urgency, do whatever it takes.

## 9.5 MEGA-SPRINT SESSION — 2026-09-14 (1:20 PM–2:20 PM EDT) — DEPLOYED ✅

**Pablo directive:** max-urgency burst, all subagents firing, make money happen. Client asked to (1) verify revenue strategy against the LIVE internet before sinking tokens, and (2) think outside the box. Squad fan-out executed: managers ran direct (this env has no second-level subagent delegation).

**LIVE-VERIFIED REVENUE INTEL (web-researched this session, from official pages):**
1. **Amazon Associates commission schedule (official page, verified):** Tools/Home/Outdoors = **3%** (weak lever); Automotive = **4.5%**; **Prime for Young Adults (18-24) = $30 signup bounty; Audible = $20-25 bounties** — our exact demographic, massively undersold.
2. **Education/trade-school lead-gen CPL = the flagship play:** UTI has a LIVE "Partner With Us" program (https://www.uti.edu/partner-with-us, verified); Lincoln Tech runs active partnerships. Our quiz→email funnel is the same mechanism schools pay for; CPL >> a $60 tool click.
3. **Raptive** ($4B paid to creators, verified) = real premium ad network but needs scaled traffic; AdSense = the on-ramp.

**SHIPPED + DEPLOYED this sprint:**
- **[x] Hawkeye:** 3 affiliate posts, 141 links total tag=tradelift-20: best-welding-safety-gear (34), best-cordless-power-tool-kits (48), best-hvac-tools (59). 22 blog posts live.
- **[x] Vision:** wired all 6 previously-unwired posts → blog.html = 22 cards + 22 BlogPosting; fixed 2 broken OG refs; restored docs/outreach-strategy.md (was misplaced at /workspaces/docs/); **fixed deploy bug** (careers.guide was being overwritten by old 5-trades PDF).
- **[x] Shuri:** CRO — exit modal rewritten (benefit-led, one CTA, trust line), microcopy + honest trust signals on index/getting-started.
- **[x] Stark:** **PAID PRODUCT #1**: 14-page "The First 90 Days in the Trades" PDF ($12 rec; assets/premium/first-90-days.pdf, 81.7KB, idempotent, salary-synced) + docs/storefront-launch-kit.md (Gumroad-ready).
- **[x] Fury:** docs/education-leadgen-playbook.md, docs/amazon-bounty-playbook.md, docs/email-sequence.md (7-emails), docs/adsense-readiness.md (privacy + consent).
- **[x] Lang:** docs/social-kit-posts.md, docs/tiktok-scripts.md, docs/quiz-share-kit.md.
- **[x] Coulson:** docs/school-outreach-emails.md (+20-school list + templates), docs/sponsorship-pitch.md ($250/$500 packages + top-10 prospects).
- **[x] QA (Rogers + Romanoff):** CONDITIONAL PASS → fixed: (1) exit-modal was gated to FIRST-EVER visit (returning visitors never saw it) → per-session sessionStorage gate + dismissed/converted localStorage flags; (2) **SECURITY:** docs/ scripts/ PROGRESS.md AGENTS.md + premium PDF + orphan 5-trades PDF were ALL shipped publicly → excluded; (3) sitemap regen moved before rsync (was never reaching build); (4) badge.html in sitemap.
- **[x] DEPLOYED + live-verified:** 12 key pages + careers.guide + roadmaps + og images all 200; **sitemap 30 locs live**; internal docs/scripts/premium PDF all 404 (protected).

**OPEN REVENUE ACTIONS (48h):** Pablo → Gumroad account + publish $12 guide; Buttondown free tier + migrate email; UTI/Lincoln partner pitches; real contact email. Jarvis → tradeschools.html hub + per-trade school landing pages + quiz-results education CTA; privacy.html; disclosed Prime-Adult bounty links; premium CTA on quiz/exit-modal.
**Known minors (next round):** BlogPosting JSON-LD missing `description`; ~44 affiliate links are /s?k= search URLs (convert worse — swap picks to /dp/ ASINs); focus-trap listener in showExitModal (idempotent dup); beforeunload trigger dead code.

### Revenue Streams (all active simultaneously)

#### Stream A — Affiliate Revenue (target: $15,000–$25,000)
- **Amazon Associates** (ID: tradelift-20): 94 live links in tools.html + 3 affiliate posts (electrician tools, plumbing tools, welding equipment). Expansion: 12+ more trade-specific gear guides with affiliate links.
- **Trade school affiliate programs:** Penn Foster, Universal Technical Institute, Ashworth College, Vocational Training — each pays $30–$80 per lead. Dedicated landing pages + CTAs from quiz funnel + email list.
- **Safety gear brands:** Milwaukee, DeWalt, Carhartt — safety gear roundups with affiliate links.

#### Stream B — Digital Products (target: $5,000–$10,000)
- **Career Fit Guide PDF** ✅ BUILT (quiz.html + quiz.js funnel already wired). Funnel: quiz → email capture → free guide → upsell.
- **Trade-specific Roadmap PDFs** ✅ BUILT (12 per-trade roadmaps, idempotent scripts). Funnel: email opt-in → roadmap download → paid upgrade.
- **Next:** paid premium guides ($5–$15) — "How to Get Your First Trade Apprenticeship," "Trade School vs College ROI Guide," "750K Open Jobs Playbook."
- **Gumroad/Lemon Squeezy storefront** for paid products.

#### Stream C — Lead Gen / Email List Monetization (target: $5,000–$10,000)
- **Formspree captures:** Newsletter (`xqpkvyjg`) + Quiz results (`xzebljww`) — both live. Migration off disposable inbox = urgent.
- **Email funnel → affiliates:** every captured email gets automated sequence (Mailchimp/ConvertKit free tier): welcome + career guide + trade school CTAs + affiliate recommendations.
- **Exit modal:** pitch career guide on exit intent (built, needs CRO polish per Shuri pending tasks).

#### Stream D — Merch / Physical Products (target: $3,000–$5,000)
- **12 merch designs** ✅ BUILT (Lang). Printful + Etsy runbook ✅ (docs/outreach-strategy.md).
- **Launch:** Printful store + Etsy listings with branded merch (t-shirts, hoodies, stickers).
- **Quiz → merch:** "I'm an Electrician" badge results page with merch CTAs.

#### Stream E — Ad Revenue (target: $2,000–$5,000, scaled with traffic)
- **Google AdSense:** once traffic ≥ 10K monthly sessions, place ads on blog pages + tools.html.
- **Setup required:** privacy policy, cookie consent (EU), ad placements in HTML.

#### Stream F — Partnerships & Sponsorships (target: $2,000–$5,000)
- **Schools/counselors:** embeddable widget → referral traffic + backlinks (SEO juice + traffic = more ad/affiliate revenue).
- **Trade organizations:** content partnerships, sponsored posts.
- **Sponsorships:** pitch to tool brands, trade schools, PPE companies once traffic hits thresholds.

#### Stream G — Social Media Traffic → Revenue (driver for ALL streams above)
- **TikTok primary** + IG Reels + YouTube Shorts (social-media-strategy.md 90-day calendar).
- **Target:** 5,300 followers, ≥5% engagement, 12% email capture from traffic.
- **Goal:** viral trade content → funnel to quiz → email → revenue streams.

### Squad Deployment (ALL revenue-focused)

| Subagent | Revenue Assignment |
|----------|-------------------|
| **Hawkeye** | Content blitz: 2-4 SEO posts/week (affiliate posts + lead-gen content), trade school affiliate landing pages |
| **Stark** | Product builder: paid premium guides, Gumroad storefront, merch integration on site |
| **Fury** | Monetization ops: AdSense setup, trade school affiliate program signups, email automation sequences, conversion funnel optimization |
| **Vision** | Revenue integration: all CTAs funnel-connected, sitemap, new pages wired immediately |
| **Shuri** | CRO: exit-modal upgrade, benefit-led microcopy, trust signals, A/B test variants |
| **Lang** | Share images (social traffic driver), merch print files, OG cards for all posts |
| **Rogers** | QA on ALL revenue pages (every new page/product/funnel goes through Rogers pass 1) |
| **Romanoff** | QA pass 2 on revenue funnels (email capture, affiliate links, checkout flow) |
| **Coulson** | Outreach: schools, counselors, trade organizations, sponsorships |

### Immediate Sprint (next session, execute in order)
1. **Fix known gaps** (wire 3 posts, regen sitemap, deploy surge.sh) → clears backlog
2. **Shuri CRO** — exit modal, microcopy, trust signals → improves conversion immediately
3. **Fury AdSense + affiliate programs** — start earning from existing traffic NOW
4. **Hawkeye** — 4 more affiliate posts (2 trade school guides + 2 gear roundups)
5. **Stark** — Gumroad storefront + 2 paid products listed
6. **Fury** — Email automation sequence (welcome + affiliate drip)
7. **Lang** — Share images for all posts (social traffic driver)
8. **Fury + Vision** — Trade school affiliate landing pages (high-CPA)
9. **All subagents** — continuous: propose revenue growth ideas every round, PM reviews

### Revenue Tracking
- [ ] Set up spreadsheet/dashboard for tracking: traffic, email captures, affiliate clicks, sales, revenue per stream
- [ ] Formspree dashboard monitoring (daily)
- [ ] Google Analytics on site (traffic sources, quiz completions, conversions)
- [ ] Amazon Associates dashboard monitoring (daily once AdSense/affiliate running)

---

## 11. SESSION — 2026-09-15 (8:00–8:45 AM EDT) — REVENUE SPRINT #2 (deployed, committed `a122220`, origin sync pending)

**Directive:** resume from mega-sprint; maximum urgency; full autonomy. Executed:

- **[Hawkeye] NEW `tradeschools.html`** — Trade Schools & Training lead-gen hub (~2200 words, CollectionPage JSON-LD, canonical surge, nav/footer w/ active). Trade-school vs apprenticeship table, 12-trade training paths (salaries = quiz.js/trades.html canonicals verbatim), top US trade schools w/ official links (uti.edu, lincolntech.edu, tulsaweldingschool.com, williamson.edu, ntma.org) + FTC disclosure, quiz CTA + newsletter funnel. High-CPA education play for Stream B.
- **[Fury] NEW `privacy.html`** — AdSense-ready Privacy Policy (+WebPage JSON-LD): Formspree/localStorage collection, future ads/analytics, CCPA/GDPR, COPPA 16+, Amazon Associates disclosure, contact placeholder `hello@tradelift.surge.sh`.
- **Wiring (all 7 main pages):** `Trade Schools` nav + footer links; every footer now has Privacy Policy link; quiz email-capture success now shows "Compare top trade schools" CTA (btn-outline → tradeschools.html); sitemap generator mainPages +2 → 32 URLs (idempotent ×2); new pages live 200.
- **SEO fix:** BlogPosting JSON-LD `description` added to all 22 entries (scripted from each post's `<meta name="description">`; 22/22, JSON valid, ≤160 chars).
- **Revenue:** resources.html "Student Money-Savers" section → Amazon Prime Student (`/gp/student/signup/info?tag=tradelift-20`) + Audible (`/Audible-Free-Trial-Digital-Membership/dp/B00NB86OYE?tag=tradelift-20`) + standard Amazon Associates disclosure.
- **Bug fixes (js/main.js):** exit-modal focus trap → idempotent (`dataset.trapBound` guard) + live focusable recompute inside handler (fixes stale-capture after success-state hides the submit button); removed dead `beforeunload` listener. `node --check` OK.
- **QA:** Romanoff Pass 2 **PASS** (0 crit/major) → fixed Diesel "Technician"→"Mechanic" naming, privacy footer Trade-Schools gap. Rogers Pass 1 **PASS** after fixes → moved privacy footer `aria-current` to Privacy link, footer link-order parity, Automotive "Technician"→"Mechanic", sitemap regen. Full sweep: 34 HTML clean, 0 dup IDs, valid JSON-LD, links resolve, title/desc limits.
- **DEPLOYED + live-verified:** new pages 200, key pages 200, sitemap 32 live, docs/scripts/premium PDF still 404 (secrets secure).
- **NEXT (Pablo):** Gumroad publish $12 guide; Buttondown + email migrate; UTI/Lincoln partner pitches; real contact email; Formspree off disposable inbox.
- **NEXT (Jarvis):** premium CTA after Gumroad; 44 `/s?k=` affiliate links → `/dp/` ASINs; GSC sitemap submit; email auto-sequence; revenue dashboard.
