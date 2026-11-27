---
name: webdev-typography
description: "Font pairing, size, line-height, readability. Use when the user asks for typography, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
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

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
