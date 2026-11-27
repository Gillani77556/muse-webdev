---
name: webdev-typography
description: "Font pairing, size, line-height, readability. Use when the user asks for typography, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-typography

**Command:** `/webdev typography <url or brief>`

Font pairing, size, line-height, readability.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `typography`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Choose one heading font and one body font; check readability on mobile.
2. Set sizes and line-height; never use more than 3 sizes for body text.
3. Check contrast for every text-on-colour pair.

## Checklist
- [ ] Headings hierarchy H1-H3 correct
- [ ] Body 16px or larger
- [ ] Line-height 1.5+
- [ ] Contrast passes


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Define the scale once in `:root` and never use a size outside it:
- Display/hero: clamp(2.5rem, 6vw, 3.5rem), weight 800, line-height 1.1.
- H1: 2.5rem (40px), H2: 2rem (32px), H3: 1.5rem (24px), body: 1.0625rem
  (17px), small: 0.875rem (14px). Line-height 1.2 headings, 1.6 body.
- Max 2 font families: one display/headings, one body. Google Fonts, max
  2 weights each. System-font fallback stack always present.
- One H1 per page; H2/H3 in logical order; never skip a level.
- Contrast: body text on paper 7:1+, text on photos always over a dark
  gradient overlay, never raw white on a bright photo.
- Letter-spacing: -0.02em on display headings, 0 on body; uppercase only
  for eyebrow labels (12-13px, letter-spacing 0.12em).

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
