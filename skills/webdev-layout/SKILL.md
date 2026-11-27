---
name: webdev-layout
description: "Hero, header, footer, sections and grid — everything in order, nothing cut off. Use when the user asks for layout, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-layout

**Command:** `/webdev layout <url or brief>`

Hero, header, footer, sections and grid — everything in order, nothing cut off.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `layout`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Sketch the page order: header, hero, proof, services, about, FAQ, CTA, footer.
2. Check every section has one job and one CTA at most.
3. Verify nothing is cut off at desktop, tablet and mobile widths.

## Checklist
- [ ] Header and footer on every page
- [ ] Hero clear in 5 seconds
- [ ] Sections in logical order
- [ ] No overflow


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Build every homepage in this exact order — a senior site is complete,
not minimal:
1. Sticky header: brand + nav + WhatsApp/call CTA.
2. Hero: large real photo, headline, subhead, 2 CTAs, trust strip
   (e.g. "Licensed tours · English-speaking guides · Free cancellation").
3. Trust bar: 3-4 short proof points (real facts only, never invented).
4. Services/Tours grid: cards with real photo, duration, highlights,
   sample price labelled "Sample price", WhatsApp CTA per card.
5. How it works: 3-4 numbered steps (enquire → confirm → pay → travel).
6. Why choose us: 3-4 real differentiators tied to the business.
7. Places/Destinations: photo strip or grid of real places.
8. Interactive planner: pick tour + guests + date → live total + WhatsApp
   message button.
9. FAQ: 4-6 real questions, working accordion.
10. Final CTA banner with photo background + WhatsApp button.
11. Footer: brand, quick links, contact (real number only), copyright.
Every inner page reuses header/footer and the same tokens. No page is a
bare list of links.

- Never invent a phone number, price, review or address. Sample prices are
  always labelled "Sample price" on every price, plus one note on the page
  saying prices are samples. No invented reviews — omit that section.
- No lorem ipsum, no placeholder text, no placeholder images
  (placehold.co, dummyimage, grey boxes). If a real photo is unavailable,
  use a designed CSS gradient panel with a real heading — never a fake photo.

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
