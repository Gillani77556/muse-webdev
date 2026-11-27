---
name: webdev-responsive
description: "Mobile, tablet, desktop — correct on every screen. Use when the user asks for responsive, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-responsive

**Command:** `/webdev responsive <url or brief>`

Mobile, tablet, desktop — correct on every screen.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `responsive`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Test at 360, 768 and 1280 pixels with screenshots.
2. Fix overflow, tiny text, overlapping elements and unusable buttons.
3. Re-test after every fix; report the widths that passed.

## Checklist
- [ ] 360px mobile clean
- [ ] 768px tablet clean
- [ ] 1280px desktop clean
- [ ] No horizontal scroll

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
