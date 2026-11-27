---
name: webdev-senior-review
description: "Senior-developer final review, 25-30 year checklist. Use when the user asks for senior-review, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-senior-review

**Command:** `/webdev senior-review <url or brief>`

Senior-developer final review, 25-30 year checklist.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `senior-review`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Review as a 25-year senior: design, code, copy, flow and trust.
2. List every gap, however small, with its fix.
3. Do not say ready until every gate passes.

## Checklist
- [ ] Every section reviewed
- [ ] Every gap listed
- [ ] No AI-looking pattern left


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Do not say "ready" until EVERY gate below passes. One fail = not ready.
- [ ] Design system exists: CSS tokens (palette, type scale, spacing,
  radius, shadows) in `:root`, used on every page.
- [ ] Hero is a large REAL photo (78vh+), headline + 2 CTAs + trust strip.
- [ ] Every tour/card/section has a REAL photo; each URL verified HTTP 200
  before use; alt text on every image; zero placeholder images.
- [ ] Interactive component present and working (planner/calculator/filter),
  tested with real inputs; totals update live.
- [ ] Full architecture: header, hero, trust bar, services, how-it-works,
  why-choose-us, places, planner, FAQ, final CTA, footer.
- [ ] Mobile-first: no overflow at 360px, tap targets 44px+, nav works.
- [ ] No lorem ipsum, no invented reviews, no invented phone/price/address;
  sample prices labelled "Sample price" on every price.
- [ ] All pages return 200, internal links unbroken, schema valid.
- [ ] The site does not look AI-made or template-made: real photos, varied
  copy, consistent but human design.
List every gap with its fix. A plain site with correct structure but no
photos, no planner and no polish FAILS this gate.

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
