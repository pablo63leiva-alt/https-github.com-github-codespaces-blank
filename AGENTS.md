# TradeLift — Agent Instructions

## What This Is
A static multi-page website promoting skilled-trade careers ("TradeLift"). Dark industrial theme (orange/yellow accents), mobile-first responsive. No framework, no build step — vanilla HTML/CSS/JS. Live at https://tradelift.surge.sh/ (Surge.sh static hosting, deploy via `bash scripts/deploy-surge.sh`). Host moved OFF GitHub Pages on 2026-09-13 (`pablo63leiva-alt.github.io/tradelift` disabled, old `blue-collar-hustle-hub` URL gone). `pages` remote (pablo63leiva-alt/tradelift) is now an archived code mirror only — do NOT push there (its old workflow re-enables GitHub Pages; it lacks `workflow` scope to change).

**DOMAIN NOTE:** `tradelift.is-a.dev` was denied by is-a.dev (not software-dev related; flagged AI-generated) — it is NOT registered. Canonicals/sitemap/og all use the github.io base. Real-domain purchase is the only path to a branded URL (then re-add CNAME).

## Pages
- `index.html` — Homepage (hero, stats, featured trades, blog teaser, newsletter, footer)
- `trades.html` — 12 trade careers with filter buttons (All/Construction/Automotive/Industrial/Skilled Craft)
- `getting-started.html` — 5-step career roadmap, apprenticeships, certifications, tools, interview tips
- `resources.html` — Tools, certifications, YouTube channels, books, websites
- `blog.html` + `blog/` — Blog index + 10 SEO posts (how-to-become-an-electrician, trade-school-vs-college, best-trades-for-16-year-olds, is-welding-a-good-career, is-trade-school-worth-it, electrician-apprentice-salary, highest-paying-jobs-without-a-degree, best-electrician-tools-for-beginners, hvac-apprentice-salary, plumber-apprentice-salary)
- `tools.html` — Trade Tools Guide, 12 starter kits (tools, gear, and prep)
- `quiz.html` — "Which Trade Is For You?" 10-question quiz + email capture funnel
- `badge.html` — share badge; `widget/quiz.html` — old embed (canonical → quiz.html)

## Assets
- `css/style.css` — shared stylesheet; MUST keep every class used by the HTML files styled (earlier HTML↔CSS mismatches — check new markup against CSS)
- `css/quiz.css`, `blog/blog-style.css` — page-scoped styles (0 bare element selectors on shared pages)
- `js/main.js` — mobile nav toggle, trade filtering, newsletter + exit modal (Formspree w/ mailto fallback), OneSignal guard; null-guarded
- `js/quiz.js` — quiz engine (10 Qs, weighted, all 12 trades reachable, share/retake/email capture; double-click locked)
- `.github/workflows/deploy.yml` — GitHub Pages auto-deploy on push to `main`
- `docs/SESSION-MEMORY.md` — MASTER MEMORY OF RECORD (read first when starting a session)
- `docs/monetization.md`, `docs/conversion-funnel.md` — revenue playbooks

## Sales Targets & Audience
Teenagers / young adults considering trade careers (electrician, welder, plumber, HVAC, etc.). Avoid student debt, high pay ($60K+), job security (750K open trade positions). Business goal: traffic → email list → $50K revenue by ~Dec 22, 2026.

## Verification Commands
- HTML well-formedness: `python3` with `html.parser` (pattern used previously)
- JS syntax: `node --check js/main.js js/quiz.js`
- CSS brace balance: count `{` vs `}`
- Sitemap: `node scripts/generate-sitemap.js` (run twice → identical, 22 URLs)

## WORKFLOW RULES (ALWAYS FOLLOW)
1. **Always use subagents (squad) for reviews** — never review only with my own tools.
2. **Two review passes after finishing** any task:
   - Review PASS 1: **Rogers** — thorough first review.
   - Review PASS 2: **Romanoff** — independent, functionality-focused.
3. Fix every real bug the passes find, then re-verify.
4. Keep `PROGRESS.md` and `docs/SESSION-MEMORY.md` updated at the end of each session.
5. Every subagent self-reviews and proposes growth/revenue improvements (PM reviews their proposals).
6. Production code changes deploy via the `pages` remote ONLY after the 2-pass review.

## Squad (subagent names)
| Name | Role |
|------|------|
| Hawkeye | Content / SEO |
| Stark | Product builder |
| Fury | Growth & monetization |
| Vision | Integration |
| Shuri | Fixes / upgrades |
| Rogers | QA Pass 1 |
| Romanoff | QA Pass 2 |
| Lang | Reserve / share images |

## Session Guidance
- Live production site: `https://tradelift.surge.sh` → deploy with `bash scripts/deploy-surge.sh` (Surge CLI, creds in surge config). `pages` remote (tradelift repo) = archived code mirror — do NOT push to it (would re-enable GH Pages via its dead workflow; also editing `.github/workflows/**` requires `workflow` scope the OAuth token doesn't have).
- **DEPLOY NOTE:** Deploy unblocked 2026-09-11 via `gh auth login --web` (OAuth token, scopes `gist`/`read:org`/`repo`, in `~/.config/gh/hosts.yml`). **CRITICAL PUSH QUIRK (2026-09-11):** the codespace's own credential helper + env `GITHUB_TOKEN`/`GITHUB_CODESPACE_TOKEN` (metadata-only `ghu_` token) shadows the stored OAuth token (`gho_`, which has push rights) — a plain `git push` gets 403. **Use this exact pattern to push:** `env -u GITHUB_TOKEN -u GITHUB_CODESPACE_TOKEN git -c credential.helper= -c credential.https://github.com.helper='!gh auth git-credential' push <remote> main`. Also use `env -u GITHUB_TOKEN gh ...` for API calls. Editing `.github/workflows/**` later needs `workflow` scope.
- Commit only when the user asks, or when the full-autonomy grant covers it (PM-approved, double-reviewed production deploys).