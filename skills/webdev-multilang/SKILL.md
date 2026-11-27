---
name: webdev-multilang
description: "Urdu/English, RTL, language switch, hreflang. Use when the user asks for multilang, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-multilang

**Command:** `/webdev multilang <url or brief>`

Urdu/English, RTL, language switch, hreflang.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `multilang`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Check the switch on every page; RTL layout must not break.
2. Verify hreflang tags and that each language page is complete.

## Checklist
- [ ] Language switch works
- [ ] RTL correct
- [ ] Hreflang correct
- [ ] No mixed-language text

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
