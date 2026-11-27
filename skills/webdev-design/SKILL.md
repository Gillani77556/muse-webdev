---
name: webdev-design
description: "Design system: colours, fonts, spacing, buttons, cards. Use when the user asks for design, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-design

**Command:** `/webdev design <url or brief>`

Design system: colours, fonts, spacing, buttons, cards.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `design`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Pick colours and fonts from the brand; never more than 3 main colours.
2. Define spacing, button, card and heading styles once and reuse them.
3. Show the system on one page before applying it everywhere.

## Checklist
- [ ] Max 3 colours + neutrals
- [ ] Max 2 font families
- [ ] Spacing scale consistent
- [ ] Buttons one style


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Before writing a single page, define the design system as CSS tokens in
`:root` and use ONLY those tokens in every stylesheet:
- **Palette:** `--color-primary`, `--color-accent`, `--color-ink`,
  `--color-paper`, `--color-muted`, `--color-line`. Max 3 colours + neutrals.
  Pick from the topic (travel → deep teal + warm sand + gold accent).
- **Type scale:** display 56px / H1 40px / H2 32px / H3 24px / body 17px /
  small 14px; line-height 1.2 headings, 1.6 body. Max 2 font families.
- **Spacing scale:** 8 / 16 / 24 / 32 / 48 / 64 / 96px. Section padding
  64-96px desktop, 48px mobile.
- **Radius:** 12px cards, 16px large cards, 24px hero panels; pill buttons.
- **Shadows:** soft `0 8px 30px rgba(0,0,0,.08)`; hover lifts to
  `0 16px 40px rgba(0,0,0,.14)`.
- **Hero:** photographic, min-height 78vh, gradient overlay, headline +
  subhead + 2 CTAs + trust strip. No hero without a real photo.
Every page reuses the same tokens — one style everywhere, nothing ad hoc.

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
