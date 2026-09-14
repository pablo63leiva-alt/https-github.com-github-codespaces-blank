# TradeLift — AdSense & Compliance Readiness

**Owner:** Fury · **Build:** Jarvis · **Legal-signer:** Pablo (ONLY-PABLO for anything needing legal identity/name, REVENUE-OPS §4 #7)
**Status:** Ready-to-paste materials + build spec. Not yet deployed; AdSense application deferred until traffic + content thresholds are real (see § blocker list).

> **Golden rule:** do not apply for AdSense with fabricated traffic. AdSense needs a live site,
> real content, and (in practice) a few weeks + organic signal. Apply only when the monthly session
> numbers below are true.

---

## A. Ready-to-paste Privacy Policy (adopt on /privacy.html — new page)

Paste into a new `privacy.html`, styled with existing `css/style.css` classes (simple content page
pattern, mirror `getting-started.html` layout), and link it in the footer (index/html + blog + quiz
footers, single shared fragment so it only lives in one place).

```html
<main class="container">
  <h1>Privacy Policy</h1>
  <p><em>Effective: [date] · Owner contact: [YOUR-EMAIL placeholder → replace with real trade email]</em></p>

  <h2>1. What TradeLift is</h2>
  <p>TradeLift (tradelift.surge.sh) is a free information site helping people explore skilled-trade
  careers. It is a static website — it has no user accounts, no databases, and no comment systems.</p>

  <h2>2. Information you give us</h2>
  <p>We collect only what you choose to type into our forms: your email address when you sign up for
  the newsletter, and (if you take the career quiz) your email address plus the trade you matched
  with. This is collected through Formspree, our form-processing service.</p>

  <h2>3. Why we collect it</h2>
  <p>We use your email to send the free guide you asked for, the quiz result and career roadmap, and
  occasional updates about trades, tool guides, and career resources. If you explicitly request
  information from a trade school through one of our sponsor/partner pages, we pass the contact
  details you submitted to that school — only the fields you filled in, and only for that request.</p>

  <h2>4. Cookies and tracking</h2>
  <p>This site is a static page, so we set no first-party cookies by default. Two things may place
  cookies or similar storage:</p>
  <ul>
    <li><strong>Amazon Associates:</strong> product and offer links on this site use the Amazon
    Associates program, which may set cookies to attribute qualifying purchases and signups.</li>
    <li><strong>Future services (Google AdSense / analytics):</strong> if we later enable display ads
    or analytics, Google may set cookies to serve/report ads. These load only after you consent in
    the consent banner (see Section 9).</li>
  </ul>

  <h2>5. Third-party processors</h2>
  <p>We work with these services to make the site work: Formspree (forms),
  [email-sending provider, e.g. Buttondown] (newsletters),
  Amazon Associates (affiliate links). Each processor handles data under its own privacy policy and
  our instructions only.</p>

  <h2>6. Your rights (incl. GDPR / EU & UK)</h2>
  <p>If you are in the EU, UK, or other jurisdictions with similar law, you have the right to: access
  the personal data we hold about you; ask us to correct it; ask us to delete it; and object to or
  restrict our processing of it. To exercise any of these, email
  [contact email placeholder]. We respond within the time the law requires (normally 30 days).</p>

  <h2>7. Data retention</h2>
  <p>We keep email submissions until you unsubscribe or ask us to remove you. When you unsubscribe,
  we stop sending to you and delete your address from our sending list on request. We never sell
  personal data, and we never share it except as described in Section 3 for schools you request info
  from.</p>

  <h2>8. Children under 16</h2>
  <p>This site is intended for people 16 and older exploring careers. If you are under 16, please
  don't submit your email without a parent or guardian joining in. We do not knowingly collect data
  from children under 16.</p>

  <h2>9. EU cookie consent</h2>
  <p>If you are in the EU/UK, a consent banner appears when you first visit. Rejecting it means no
  ad/analytics cookies load; you can still use the entire site. You can change your choice later by
  clearing site data or using the banner again.</p>

  <h2>10. Changes to this policy</h2>
  <p>We update this page when we change what we do with data. The version above is current; check
  back if you're concerned. Significant changes will be flagged on the homepage.</p>

  <h2>11. Contact</h2>
  <p>TradeLift · [contact email placeholder — replace throughout before going live]</p>
</main>
```

**Placeholders to replace before deploy:** every `[contact email placeholder]` and the `[date]` +
`[email-sending provider]` line. Owner: Jarvis fills values, **Pablo confirms legal-name line items**
(none currently required, but PRP §4 #7 covers any that appear).

---

## B. Cookie-consent approach (EU/UK) + dependency-free vanilla-JS spec

**Approach:** a lightweight consent gate, not a framework. TradeLift is static — a few lines of
vanilla JS that (1) show a banner, (2) record consent in `localStorage`, and (3) only then load
third-party tags (AdSense/analytics). No consent → no third-party scripts load, site fully works.

**Why this shape:** GDPR/ePrivacy doesn't require cookie banners *per se*, but EU traffic makes a
feature-valid consent gate the safe play, and AdSense's own consent requirements layer on top.
Banner-first beats script-first: don't load analytics before consent.

**Placement:** a `<div id="cookie-banner">` fixed to bottom, non-modal (page stays usable, scroll
still allowed), two buttons: "Accept" and "Reject" (equal weight, no dark patterns), plus a "Privacy
Policy" link.

**Spec (Jarvis, ~30 min build, no libraries):**
```html
<!-- fragment on every page, or injected by js/main.js (shared) -->
<div id="cookie-banner" role="region" aria-label="Cookie consent" hidden>
  <p>We use cookies only if you accept them — for ads and analytics IF EU visitors. Quick link:
     <a href="/privacy.html">Privacy Policy</a>.</p>
  <button data-cookie="accept">Accept</button>
  <button data-cookie="reject">Reject</button>
</div>
```
```js
// js/main.js addition (null-guarded, consistent with existing style)
(() => {
  const KEY = 'tradelift_consent';
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;
  const saved = localStorage.getItem(KEY);
  if (saved === 'accepted') loadThirdParty();      // ads/analytics only after 'accepted'
  if (saved !== null) return;                        // 'accepted' or 'rejected' -> hide
  banner.hidden = false;
  banner.querySelectorAll('[data-cookie]').forEach(b =>
    b.addEventListener('click', () => {
      localStorage.setItem(KEY, b.dataset.cookie);
      banner.hidden = true;
      if (b.dataset.cookie === 'accepted') loadThirdParty();
    }));
  function loadThirdParty() {
    // placeholder for AdSense `<script async>` + Plausible/GA4 tag insertion
  }
})();
```
Non-negotiables in the build: no third-party script runs before consent; consent stored in
`localStorage`; banner hidden once answered; a way to change the choice later (clear storage or a
footer "cookie settings" link). Honor the Privacy Policy Section 9 wording on the banner.

---

## C. Ad placement map — only once sessions ≥10K/month

AdSense demand + our RPM reality (career/education ~$2–$8 CPM, US-top) means display ads are a
**passive layer**, not any meaningful part of the $50K math. Enable only when the thresholds below
are real, and only on pages that don't own conversion.

| Page | Ad status | Why |
|------|-----------|-----|
| `blog/*` (in-content, after ~40% scroll) | ✅ ENABLE first | readers are in consumption mode; in-content mid-article = standard, least intrusive |
| `resources.html` | ✅ ENABLE second | reference list, low emotion, ad-resistant to conversion loss |
| `tools.html` | ⚠️ ENABLE only as leaderboard-top / bottom, NOT product-adjacent | tool links are affiliate money makers; ads near them cannibalize clicks |
| `index.html` | ⚠️ bottom/footer slot only | homepage is brand trust; no top-of-fold ads |
| `getting-started.html` | ❌ AVOID | mid-funnel action page; keep it clean |
| `quiz.html` + `tradeschools/*` request-info pages | ❌ ALWAYS AVOID — even when traffic ≥10K/mo | conversion pages: email capture + CPL + quiz completion are the money. Any ad next to a CTA drags opt-in/letter-of-intent rates; not worth the cents. |

**Orchestration rule:** banner + in-content on ad-enabled pages; `ads.txt` added at /ads.txt with
the publisher ID (AdSense requires it); dummy-ad placeholder or dynamic slot not needed — AdSense
auto-fills. Pageview math check before flipping: ≥10K sessions/mo AND ≥3 pages/session → ~30K
pageviews → ~$60–240/mo at $2–8 RPM. That is the reason to keep it enabled, and also the reason we
never prioritize it over the list.

---

## D. Current blockers list (deploy order)

1. **No privacy.html yet** — Section A is paste-ready; Jarvis builds + links in footers (this week, no deploy).
2. **Contact email is a disposable inbox** — the placeholder `[contact email]` cannot be a throwaway
   for a legal/privacy page. → Pablo: create/forward a real environment-appropriate address; then
   Jarvis swaps the placeholder everywhere (also unblocks Formspree migration + GSC).
3. **Zero/first-week traffic is real but AdSense-optimistic** — AdSense needs live original content
   + ~1 month of natural signal. We do NOT apply until §C's ≥10K sessions re-run 2 consecutive weeks.
4. **Content count** — AdSense historically wants meaningful content (this is not a hard published
   number; quality + volume matters). We're at 15 posts + 7 pages; target ~25–30 before applying.
5. **No archived consent state on old visitors** — anyone who visited pre-banner isn't tracked (fine,
   we set no cookies today). Banner applies after deploy.
6. **ads.txt not yet present** — needed only at apply time (drop `/ads.txt` with publisher ID, owner: Pablo has the Publisher ID once the account is approved on his identity, §4 #1/#7).
7. **`robots.txt`/sitemap already healthy; GA4/Plausible tag not set** — consent-gated analytics tag
   lands together with the banner so consent controls it (Jarvis, one commit).
8. **Legal-identity sign-off** — Pablo reviews the final privacy page before first live, per §4 #7
   (it's a static site; no formal "legal name" requirement, but the contact address must be Pablo's
   call).

---

*Summary discipline: AdSense is the last-resort layer of the model. Everything in this file exists
so that when traffic arrives we flip it on legally and quickly — but the home this quarter's revenue
lives, stays the email + products + partner lanes documented in REVENUE-OPS §1.*