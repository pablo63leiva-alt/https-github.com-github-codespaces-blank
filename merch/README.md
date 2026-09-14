# TradeLift Merch — Upload Guide (Pablo's steps)

Designs are ready to sell. 12 files in `merch/designs/`:

- `<slug>.png` — 3000×3000 RGBA print file (300 DPI = 10 in print area, ideal chest print)
- `<slug>.svg` — editable source (re-tint accent color, change slogan, re-render with `node merch/generate-merch.js`)

Regenerate anytime: `node merch/generate-merch.js` (Playwright renders SVG → PNG, then self-checks
3000×3000 & >150 KB per file). All 12 slugs match `js/quiz.js`.

---

## A. Printful (picks mockups, DTG print, ships)

1. Create a free account → **Stores** → **Add your online store** → select **Etsy** (connect now, or
   disconnect later — you can still add products without one).
2. From a catalog or your custom garment, pick a product you have inventory plans for:
   - Budget: **Gildan Heavy Cotton T-Shirt, 18000** (current bestseller for trade tees)
   - Premium: **Next Level Premium T-Shirt**
   - Also load the same file to **Hoodies** (Gildan 18000 Hoodie) later — hoodie margin is higher.
3. **Add product** → **Upload design** → drop in `merch/designs/<slug>.png`.
4. Mockup tips:
   - Start with the **large chest print** placement.
   - Add a black shirt mockup + a light heather mockup so the dark slab reads correctly on both.
   - Printful will warn if the file is outside safe zone — 3000×3000 at 300 DPI is already sized right.
5. Name the product the **Etsy listing title** (copy from `launch-kit.md`), set retail to the price rec.
6. Printful generates *your* product listing preview — **do NOT publish directly yet**. You'll build the
   real listing in Etsy (↓) and pull Printful's mockup images into it.

## B. Etsy (where the listing lives)

1. **Shop setup:** Etsy shop → import/use the Printful mockups for the listing gallery.
2. **New listing → Use a template** (build one once, then duplicate):
   - **Photos (10):** 3–4 mockups (black + charcoal + heather + navy shirts), 1 back-of-shirt, flat badge
     detail shot, lifestyle "wearing it on site" shot. First image = black tee, most gift-y pose. That is
     your thumbnail — make it scroll-stopping.
3. **Copy** — from `merch/launch-kit.md`:
   - **Title** ≤140 chars: keyword + humor + occasion. Paste as-is, don't shuffle words.
   - **Description:** 3-line hook first (the buyer reads 1 line before tapping More). Add: fits/sizing,
     print care (wash cold, inside-out), mockup disclaimer ("color may vary slightly", "mockup ≠ real
     photo — styling for your gift"), and the crew-bundle note from launch-kit.
   - **Tags:** all 13 from the kit verbatim (≤20 chars each, no commas).
4. **Print product is a digital deliverable?** On Etsy, Printful items are **physical goods** → set
   **Processing time** (Printful suggests ~1–3 days + transit), shipping profile from Printful (they push
   DTG "make-to-order" = no inventory to carry).
5. **Price:** set to the price rec in the kit ($32.99 / $36.99 tiers). Use the "Maybe later" on sales
   promos for the first 30 days — let reviews accrue before discounting.
6. **Variations:** add sizes S–2XL (Gildan goes to 3XL/5XL for extra margin) and the garment/tier choice.

## C. Launch order & checks

1. First 4 to validate demand: **electrician, plumber, welder, automotive-mechanic**.
2. Then: **hvac-technician, diesel-mechanic, carpenter**.
3. Niche-royalty slots next: **ironworker, pipefitter, mason, roofer, construction-manager**.
4. After 48h: check Etsy Search Analytics (Search Terms) → add any buyer keywords you missed into
   description body text (keyword stuffing in tags/title doesn't convert — plain language in the
   description is what Etsy's search reads next).
5. Run a $5–10/day Etsy Ads trial on the **2 lower-saturation winners** (see REPORT — HVAC, ironworker/
   pipefitter) to prove margin before scaling.

## Safe-print notes

- Transparent corners are intentional (slab badge design). Print as-is; **do not** add white flood under
  the design — the accent + white palette is already shirt-color agnostic.
- If a print shop asks for a smaller file, keep it ≥ 2000×2000 for chest prints; never let them "auto-crop".
- One-color DTG keeps print cost low and speeds production — that's already how these are designed.