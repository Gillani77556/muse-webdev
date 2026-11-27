---
name: webdev-design
description: "Design system: colours, fonts, spacing, buttons, cards. Use when the user asks for design, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
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

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
