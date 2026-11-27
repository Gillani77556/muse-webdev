---
name: webdev-pixel-perfect
description: "Pixel-perfect check: spacing, alignment, overflow, cut-off text. Use when the user asks for pixel-perfect, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-pixel-perfect

**Command:** `/webdev pixel-perfect <url or brief>`

Pixel-perfect check: spacing, alignment, overflow, cut-off text.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `pixel-perfect`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Screenshot desktop and mobile; measure spacing and alignment.
2. Flag every overlap, cut-off and uneven gap with its location.
3. Re-check after fixes at the same widths.

## Checklist
- [ ] Spacing even
- [ ] Alignment straight
- [ ] No overflow
- [ ] No cut-off text


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Measure every item below at 360px, 768px and 1280px and record the numbers:
- [ ] No horizontal overflow at any width (document.scrollWidth <=
  innerWidth at 360/768/1280).
- [ ] Every image is a real photo, loads (HTTP 200), correct aspect ratio,
  no distortion, alt text present.
- [ ] Hero is full-bleed, min-height 78vh, headline never cut off.
- [ ] Card grids align: equal heights per row, equal gaps, images same ratio.
- [ ] Tap targets 44px or larger on mobile; nav usable without zoom.
- [ ] Sticky header never covers section headings (scroll-margin-top set).
- [ ] FAQ accordion opens/closes; planner updates totals live.
- [ ] No placeholder text, no lorem ipsum, no grey-box images.
- [ ] Footer complete on every page: brand, contact, links, copyright.
Report the measured widths and the image count with each URL's HTTP status.

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
