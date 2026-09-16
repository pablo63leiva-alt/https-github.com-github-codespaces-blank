# TableText — Consent & Privacy Compliance Deliverable

> **Author:** Nakia (Compliance) · **Manager:** T'Challa · **Date:** 2026-09-16 · **Status:** Ready for M'Baku QA + Ramonda pilot onboarding
> **Scope:** US product, TCPA / 10DLC / CTIA-correct. Applies to any SMS provider (written for the no-code MVP: Tally.so form + Carrd landing + SimpleTexting; consent language is provider-neutral).
> **Source of truth:** §3 "Compliance (CRITICAL — TCPA / 10DLC / A2P)" of `docs/vibe-smart-loyalty.md`.

---

## 1. Consent Disclaimer Line (landing-page form)

### 1.1 The 11 elements (mapped to the approved template)

The template in the brief is used **verbatim in structure** — all 11 elements present, in order. Do not delete or reword elements; you may only swap in the restaurant's real values.

| # | Element | Copy |
|---|---|---|
| 1 | Brand Name | [RESTAURANT NAME] bolded at line start |
| 2 | Keyword | **KEYWORD** bolded |
| 3 | Number | **(123) 456-7890** bolded |
| 4 | Autodialer agreement | "you agree to receive promotional messages sent via an autodialer" |
| 5 | Terms of Service link | (**website.com/terms**) |
| 6 | Privacy Policy link | (**website.com/privacy**) |
| 7 | Not a condition of purchase | "This agreement isn't a condition of any purchase." |
| 8 | Message frequency varies | "Message frequency varies." |
| 9 | Message & data rates | "Message and data rates may apply." |
| 10 | STOP | "Reply STOP to opt out;" |
| 11 | HELP | "HELP for more information." |

### 1.2 (a) Checkbox copy — exact text, paste in the form

Plain English. This is the recorded consent on the form:

> I agree to receive promotional text messages from [RESTAURANT NAME] at the phone number I entered. Message frequency varies and message/data rates may apply. Reply STOP to opt out; HELP for help. This is not a condition of any purchase.

Note: the full 11-element disclosure (1.3 / 1.4) sits directly under the checkbox, **unbolded, at label size**, so checkbox and disclosure are read together. The checkbox must be **off by default** — never pre-checked.

### 1.3 (b) Placeholder version (keyboard-letter, for templates)

Use this when the restaurant isn't chosen yet. This is the canonical, provider-neutral line:

> **[RESTAURANT NAME]:** By texting **[KEYWORD]** to **[(555) 555-5555]**, you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service (**[website.com/terms]**) and privacy policy (**[website.com/privacy]**). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.

### 1.4 (c) Filled-in example (demo restaurant for pilots / Okoye's demo)

**Demo values:** Restaurant = "Ember & Oak" · Keyword = `TABLE` · Number = (555) 012-3456 · Terms/privacy on `emberandoak.com`.

> **Ember & Oak:** By texting **TABLE** to **(555) 012-3456**, you agree to receive promotional messages sent via an autodialer. You also agree to the terms of service (**emberandoak.com/terms**) and privacy policy (**emberandoak.com/privacy**). This agreement isn't a condition of any purchase. Message frequency varies. Message and data rates may apply. Reply STOP to opt out; HELP for more information.

### 1.5 Form-flow note (for Shuri² / Namor)

Our funnel collects the phone number via the form rather than the customer texting the keyword. TCPA prior-express-written-consent is satisfied by the **checkbox + full disclosure on the form**; the keyword text-in line remains the compliance-canonical wording so the same line works verbatim if any restaurant later uses a text-in keyword flow (SimpleTexting keyword). The welcome/confirmation SMS should repeat the essentials: brand name, message frequency varies, and Reply STOP / HELP.

---

## 2. Privacy Blurb (form footer)

Short, consumer-facing. Paste under the form, above or beside the submit button:

> We collect your name and phone number (plus your email and birthday if you share them) so we can text you offers, promotions, and event updates. We never sell your information. You can opt out anytime by replying STOP. Read our full privacy policy here: **[link]**.

Rules: keep to 3–4 lines, plain language, no legalese. The "**[link]**" points to the section-3 policy page. If the footer gets longer than the blurb, everything beyond these two sentences moves to the full policy.

---

## 3. Full Privacy Policy Skeleton (paste-ready for the restaurant site or our hosted page)

Paste sections below (placeholders in `[brackets]`). Owner records the URL in the consent line (§1.3).

---

### Privacy Policy — [RESTAURANT NAME]

**Effective date:** [DATE] · **Last reviewed:** [DATE]

#### 1. What this policy covers
This policy explains what information we collect when you sign up to receive text messages and marketing from [RESTAURANT NAME] ("we" / "us"), how we use it, and the choices you have. It applies to our text-message program ("TableText" forms, QR-code signups) and our website [WEBSITE URL].

#### 2. Information we collect
- **Required at signup:** your name and mobile phone number.
- **Optional at signup:** your email address and birth month/day (used only for offers you opt into, such as a birthday special).
- **Automatic record of your consent:** when you check the consent box we record the date/time (UTC), the phone number, your name, the IP address of the device used to sign up, the version of the form you saw, and the campaign/keyword. This record proves you authorized the messages.

#### 3. How we use your information
- To send you promotional text messages you agreed to receive: weekly specials, limited-time offers (for example, a Monday BOGO), birthday messages, and event notices.
- To honor your requests: processing "STOP" opt-outs, updating preferences, and responding to "HELP".
- To comply with the law: checking numbers against the National Do-Not-Call (DNC) Registry, honoring consent records, and responding to legal requests.

#### 4. Your consent — how you authorize messages
When you check the consent box on our signup form you agree to receive promotional text messages sent via an autodialer at the number you provided, under our Terms of Service and this Privacy Policy. This is **not a condition of any purchase**. Your consent is logged and retained (see Section 8). You may revoke it at any time — see Section 6.

#### 5. Do-Not-Call and mandatory disclosures
We screen message recipients against the National DNC Registry and do not target numbers listed without their prior written consent. Every promotional message begins with our brand name and includes opt-out instructions; we send at least one "Reply STOP" reminder per month.

#### 6. Opt out / STOP (your choice)
- **By text:** reply **STOP** to any message. You will receive one confirmation that you have been unsubscribed, after which no further messages will be sent to you.
- **By email:** contact us at [PRIVACY EMAIL] and request removal.
- You will not be re-added unless you actively sign up again.
- For help, reply **HELP** to any message or email [PRIVACY EMAIL].

#### 7. Sharing — we do not sell your data
We never sell or rent your personal information. We share it only with the service providers needed to run the program:
- **Our software provider** [e.g., TableText] — maintains the signup forms, consent logs, and customer lists.
- **Our SMS messaging provider** [e.g., SimpleTexting] — stores consent records and delivers the text messages.

These providers process data solely to provide the service and are contractually prohibited from using it for their own marketing.

#### 8. Data retention
- **Active subscriber data:** kept while you remain subscribed to the text program.
- **Consent records and opt-out records:** retained for at least as long as the subscriber relationship, and in any case no less than [5] years from the date of consent, to preserve proof of authorization. ([Recommendation under review by counsel.])

#### 9. Your privacy rights
If you are a California resident, the California Consumer Privacy Act (CCPA) gives you the right to:
- **Know** what personal information we collect, use, and share.
- **Delete** your personal information (subject to legal exceptions).
- **Correct** inaccurate personal information.
- **Opt out of sale/sharing** — we do not sell your data, so there is nothing to opt out of.

If you are in any U.S. jurisdiction, the Telephone Consumer Protection Act (TCPA) gives you the right to revoke message consent at any time (reply STOP) and to be placed on our internal do-not-contact list. We honor these rights without discrimination.

#### 10. Children
This service is not directed at children under 13, and we do not knowingly collect their information. If you believe a child provided us their data, contact [PRIVACY EMAIL].

#### 11. Contact
Questions about this policy, your data, or the text program: **[PRIVACY EMAIL]**. For text support, reply HELP to any message.

#### 12. Changes to this policy
We may update this policy; the "Last reviewed" date at the top reflects changes. Material changes will be noted on this page and, where required, announced in a program message.

---

## 4. Consent-Logging Spec (for M'Baku QA)

### 4.1 What to store per opt-in (the record of consent)

| Field | Format / example | Required |
|---|---|---|
| consent_id | UUID, e.g. `9f8d…` | Yes |
| restaurant / brand | `Ember & Oak` | Yes |
| phone | E.164, e.g. `+15550123456` | Yes |
| name | as entered on form | Yes |
| consent_timestamp_utc | ISO 8601 UTC, e.g. `2026-09-16T18:03:22Z` | Yes |
| form_copy_version | e.g. `v1.2` | Yes |
| form_copy_hash | SHA-256 of the exact checkbox + disclosure text served | Yes |
| ip_address | IPv4/IPv6 of signup device | Yes |
| campaign / keyword | e.g. `TABLE`, `mon-bogo`, `welcome` | Yes |
| source_channel | `QR-tent` / `landing-URL` / `keyword-text` | Yes |
| provider_message_id | SimpleTexting message ID of the confirmation SMS, if available | If available |
| list_id / group | SimpleTexting list the contact was added to | Yes |
| status | `active` / `opt-out` / `soft-bounce` | Yes |

### 4.2 Where the records are stored (no-code MVP)

- **SimpleTexting consent log.** Per the brief, SimpleTexting has built-in compliance tooling and logs consent records per contact (keyword/source, opt-in time, list) — the provider audit trail.
- **Tally.so response export = our independent source-of-truth file.** Tally captures response timestamp and respondent IP at submission. Export to **CSV and/or Airtable** — one row per submission, retaining the consent timestamp, IP, entered values, and the form version the customer saw.

Rule for the MVP: **the Tally export is the authoritative consent artifact** and must be exported to CSV/Airtable for every restaurant **no later than end of week** (SimpleTexting's log is the live operational record; the CSV/Airtable copy is the retrievable, court-ready evidence).

### 4.3 Retention

- Consent + opt-out records: keep for the lifetime of the subscription **plus a minimum of 5 years** (recommend 7 years) from the last activity, to cover TCPA claim windows. Archive in the restaurant's folder in Airtable/S3; do not delete on list purge alone.

### 4.4 Proof-of-consent retrieval process (documented)

1. Receive request (customer, carrier, or legal) referencing a phone number and date.
2. Search Airtable/CSV archive by phone (E.164) → pull consent record: timestamp UTC, form version + hash, IP, campaign.
3. Cross-reference SimpleTexting consent log for the same number (provider message ID, keyword).
4. Reassemble both into a single export (CSV/JSON) and attest: checkbox present (copy matches form_copy_hash), disclosure was the then-current version, timestamp precedes the first promotional blast.
5. Log the retrieval request itself (requester, date, result) for audit trail.

---

## 5. STOP / HELP + Opt-Out Automation Checklist (provider requirements)

The SMS platform **must** do the following automatically (user-level consent is handled in §1):

- [ ] **STOP processed instantly** — any of `STOP`, `STOPALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT` (case-insensitive) removes the number from all promotional lists immediately on receipt.
- [ ] **Auto opt-out confirmation** sent once: "You're unsubscribed from [RESTAURANT NAME] texts. No further messages will be sent. Reply HELP for help." No promotional content.
- [ ] **Never text a stopped number again** — no re-add, no campaign imports that resurrect the number, no "one-click" resubscribe — except the single opt-out confirmation. A fresh, standalone opt-in (new checkbox, new form) is the only path back.
- [ ] **HELP handled automatically** — "For help with [RESTAURANT NAME] texts, reply or contact [support contact]. Msg freq varies; msg & data rates may apply." Returns the brand name, frequency, and rates per CTIA guidance.
- [ ] **Compliance keywords case-insensitive** and trimmed of surrounding whitespace.
- [ ] **Provider-level suppression** persists across segments/lists (not just one list).
- [ ] **Opt-out recorded in the consent log** (status → `opt-out`) and surfaced in the monthly DNC/retention report.
- [ ] **No automated resubscribe prompts** (e.g., "text YES to resubscribe") unless approved by compliance — the brief's rule is one-click resubscribe is prohibited; resubscribe only via fresh written consent.

---

## 6. Sending Guardrails (hard rules, from the brief)

| Guardrail | Rule |
|---|---|
| Time-of-day window | Send only **8:00 AM–9:00 PM** recipient local time. **Florida and Oklahoma: 8:00 AM–8:00 PM** local. Schedule engine must compute recipient-local time. |
| Frequency cap | **Hard cap 2 texts/week per subscriber TOTAL** (welcome counts). Default plan uses exactly 2 slots: 1 promotional offer blast + 1 welcome/lifestyle/birthday. Any increase requires compliance sign-off. |
| "Reply STOP" reminder | **At least one per month** per subscriber (CTIA), appended to or delivered as a promotional message. |
| Brand name | Every message **starts with the brand name** (e.g., "Ember & Oak: …"). |
| DNC scrub | Every number scrubbed against the **National DNC Registry** before each blast; internal suppression list (STOPped numbers) always honored. |
| Welcome/confirmation | First SMS on signup confirms the opt-in, restates brand, frequency, rates, and STOP/HELP. |
| Content | Promotional only to opted-in numbers; no illegal/harmful content; offers match the campaign keyword ("mon-bogo", "birthday"). |

---

## 7. Pre-Launch Compliance Checklist (restaurant owner — 12 items, sign before first blast)

1. **10DLC brand registered** (TCR, one-time ~$4.50) with restaurant's EIN/SSN details.
2. **10DLC marketing campaign registered + approved** (vetting + monthly fee) with the provider.
3. **Number provisioned** (local/long code) and tested — sending and receiving both work.
4. **Consent line on form** is the exact 11-element copy (§1.3) with real brand, keyword, number, and working ToS/privacy links; checkbox **unchecked by default**.
5. **Privacy blurb** (§2) on form footer and **full privacy policy live** (§3) at the linked URL.
6. **Consent logging on:** Tally responses exporting to CSV/Airtable (§4) and SimpleTexting consent log verified with a real test signup.
7. **STOP/HELP test:** a live test number replies STOP → receives opt-out confirmation → receives no further messages (§5). HELP reply → help message.
8. **Monthly "Reply STOP" reminder** templated and scheduled into the campaign calendar.
9. **DNC scrub** run on the starting list (empty at launch, but know the procedure) with zero numbers skipped.
10. **Blast schedule set** to the §6 windows (8 AM–9 PM local; FL/OK 8 AM–8 PM) with the ≤1/week frequency cap enforced on the first campaign.
11. **Every outbound template** starts with the brand name and includes opt-out language.
12. **Compliance sign-off recorded:** Nakia (consent log + wording) and M'Baku (functional STOP/HELP + retention) each pass, documented in the restaurant's folder.

Rule: **no first blast before all 12 are checked.** Address items 4, 6, 7, and 12 with the TableText squad, not self-certified alone.

---

## 8. Risks If Skipped

| Risk | What happens | How this doc prevents it |
|---|---|---|
| **TCPA penalties — $500–$1,500 per violating message** | Each promotional text sent without valid consent (or after STOP) carries a private right of action of $500–$1,500 per message, paid by the restaurant. 100 bad messages = $50k–$150k exposure. | §1 consent line (checkbox + verbatim 11-element disclosure), §4 consent records, §5 instant STOP suppression. Numbers with provable consent are the defense. |
| **Carrier blocking of unregistered 10DLC traffic** | Unregistered A2P/10DLC traffic is filtered and blocked by US carriers — messages get silently black-holed or rejected, the list dies, and the restaurant's reputation with providers erodes. | §7 items 1–3: brand + campaign registration before launch, verified number. |
| **Class actions on consent gaps** | Aggregated TCPA suits over missing/ambiguous consent, pre-checked boxes, or messaging that ignores STOP responses. Defense requires records, not memory. | §1 checkbox off-by-default + verbatim disclosure; §4.4 documented proof-of-consent retrieval so we can produce a per-number record on demand. |
| **List decay / carrier complaints** | Over-texting drives 53% of opt-outs (brief, market research) and spam complaints that trigger carrier filtering. | §6 frequency cap ≤1/wk, time windows, monthly STOP reminder keep sends reasonable and complaints down. |

**Net position:** with §1–§7 in place, every sent message traces to a logged, retrievable consent record; every opt-out is immediate and permanent; and the brand's 10DLC registrations are current. The residual risk is the cost of the registrations and the weekly discipline of using the guardrails — not a penalty line.