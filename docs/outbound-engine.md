# Outbound Engine — The "Get It OUT THERE" Master Plan (all tracks)

**Owner:** Jarvis (PM) · **Created:** 2026-09-16 · **Directive:** "Don't just build products — MARKET them. Ads. Distribution. Everything."
**The shift:** Build mode → Distribution mode. We now market what's built BEFORE building more.

---

## 0. The principle

> Revenue = Offer × Traffic × Conversion. Traffic is the bottleneck. Every hour goes to getting the 32 posts, 2 funnels, guide PDF, merch, and TableText kit in front of eyes — not to another PDF.

---

## 1. The three engines, run in parallel

| Engine | What it does | Assets ready | Blocked on Pablo |
|---|---|---|---|
| **Paid Ads** | Meta/TikTok/Google campaigns → quiz + gear + guide | docs/ads-kit.md (copy, audiences, budgets, scale gates) | Ad accounts + pixel IDs (~30 min) |
| **Organic Social** | TradesFlicks short-form brand → quiz funnel | docs/tradesflicks-brand.md (30 vids, hooks, cadence) + existing tiktok-scripts/social-kit | Account creation (~20 min) |
| **Outreach / PR** | HARO, Reddit, schools, counselors, sponsors | docs/haro-reddit-kit.md, school-outreach-emails, outreach-strategy, sponsors | Email account / sending |

---

## 2. Ready-to-fire actions (need only 30-60 min of Pablo)

**Top 5 by revenue-leverage:**
1. **ASIN swap (10 min)** — paste real ASINs into `scripts/asins.csv` → `python3 scripts/verify-asins.py --apply` → gear links convert properly.
2. **Publish the $12 guide on Gumroad (15 min)** — listing copy ready in `docs/storefront-launch-kit.md`; file = `assets/premium/first-90-days.pdf`. Link it in quiz email-success + exit modal.
3. **Create TikTok/IG/YT + set 'Take the quiz' in bio (15 min)** → hand Jarvis the handles; I publish the first week of posts.
4. **Create Meta + TikTok Ads accounts (15 min)** → share pixel/account ID → I install base pixels + event schema + write UTM-ready URLs.
5. **Buttondown (free) takeover (15 min)** → import Formspree emails → 7-email sequence ready (`docs/email-sequence.md`).

**Next tier (this week):**
6. UTI / Lincoln Tech partner pitch (email template + prospect list ready) — CPL revenue.
7. Send first pilot outreach batch from `docs/tabletext-pilot-leads.csv` (20 leads, templates in tabletext-pilot-outreach.md).
8. HARO: register free account, set keyword alerts (kit is ready).

---

## 3. Daily rhythm I (Jarvis) can do WITHOUT Pablo (start now)

- [x] Write + stage next 30-day TradesFlicks video pack (done — tradesflicks-brand.md)
- [x] Write ad copy + budgets for all 4 campaigns (done — ads-kit.md)
- [ ] Draft next 2 posts: **blog/best-cordless-glue/impact drivers** OR **best-work-pants-for-trades** OR **best-ear-protection** (gear affiliates — more Amazon commissions) → then QA + deploy
- [ ] Build the UTM audit script so every link gets tagged (grep check on CI)
- [ ] Pre-build pixel snippet (ID placeholder) ready to paste into js/main.js
- [ ] Draft the 8-week content pipeline for Track C (bank of 60 hooks)

---

## 4. Progress gates (check weekly)

| Metric | Target (90 days) |
|---|---|
| Quiz emails captured/month | → 500+ |
| Quiz completions/month | → 2,000+ |
| Video views/month (all platforms) | → 250K |
| Gear clicks/month | → 8,000 |
| Guide sales | → 50+ |
| Amazon earnings/month | → $500+ |
| CPL school leads (post-partnership) | → 20/mo |
| TableText pilot restaurants | → 2 signed |

---

## 5. What to stop doing

- ❌ No more docs that don't drive distribution (build only if it reaches people)
- ❌ No more unpaid account work Pablo "should" do — if it can wait, it waits; marketing first
- ❌ No more silent product launches — every product ships WITH a marketing hook (ad/script/outreach)

---

## 6. Immediate next moves (Jarvis, today, no Pablo needed)

1. Build 2 more gear posts (ear protection + work pants) → QA → deploy (grows the Amazon pool)
2. Write pixel-ready snippet + event schema → hand to Pablo with a 10-line "paste this in"
3. Stage TradesFlicks week-1 scripts (7 videos with captions + hooks) → Pablo shoots back-to-back in < 1 hour
4. Draft the UTI/Lincoln cold-email (ready to send when Pablo's email is live)
5. Update memory docs