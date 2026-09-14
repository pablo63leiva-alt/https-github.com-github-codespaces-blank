# TradeLift — Career Roadmap PDFs

The 12 free roadmaps promised by the quiz funnel (`js/quiz.js`) after email capture.
Each is a clean 2-page PDF (dark industrial theme, orange `#ff6b00` accent) produced by
`scripts/generate-roadmaps.py` (idempotent — rerun to regenerate byte-identical files).

## Trade → file → salary band

Salary bands are exactly the site figures: `trades.html` "Average Salary" equals the quiz
result shown in `js/quiz.js` (identical strings). BLS medians cited below come from the site's
own salary blog posts so the PDFs never contradict published content.

| Trade | File | Journeyman band (site) | Band source / assumptions |
|---|---|---|---|
| Electrician | `electrician-roadmap.pdf` | $60K–$80K | Blog-cited (see salary note). |
| Plumber | `plumber-roadmap.pdf` | $55K–$75K | Blog-cited (see salary note). |
| Welder | `welder-roadmap.pdf` | $45K–$70K | Blog-cited (see salary note). |
| HVAC Technician | `hvac-technician-roadmap.pdf` | $50K–$70K | Blog-cited (see salary note). |
| Automotive Mechanic | `automotive-mechanic-roadmap.pdf` | $40K–$65K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |
| Carpenter | `carpenter-roadmap.pdf` | $45K–$65K | Blog-cited (see salary note). |
| Ironworker | `ironworker-roadmap.pdf` | $55K–$80K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |
| Pipefitter | `pipefitter-roadmap.pdf` | $60K–$85K | Blog-cited (see salary note). |
| Diesel Mechanic | `diesel-mechanic-roadmap.pdf` | $45K–$65K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |
| Mason | `mason-roadmap.pdf` | $45K–$70K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |
| Roofer | `roofer-roadmap.pdf` | $40K–$65K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |
| Construction Manager | `construction-manager-roadmap.pdf` | $70K–$100K | **ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js. |

## Assumptions

- bands marked **ASSUMED** have no dedicated salary post on the site (dedicated posts exist
  only for electrician, plumber, welder, HVAC, carpenter). Their headline band is the canonical
  `trades.html` + `quiz.js` figure; no external median is printed in those PDFs.
- carpenter: the headline band is the site figure `$45K–$65K`; the blog post narrows "journeyman"
  to `$44K–$60K` with a $51,390 BLS median — the PDF prints the site band and cites the median.
- plumber: `$55K–$75K` per trades.html, quiz, and the plumber blog's own headline ($59,880 median).
- pipefitter: BLS $59,880 cited on site as the combined plumbers & pipefitters median.
- slugs match the canonical `id` values used in `widget/quiz.html` and the site's 12-trade order.

## Verification

`python3 scripts/generate-roadmaps.py` performs: file existence, `>10KB` size check, pypdf
reopen + 2-page + text extract assertions, and a `js/quiz.js` name/salary string sync check.
