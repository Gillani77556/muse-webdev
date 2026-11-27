---
name: webdev-fix
description: "Find the fault, fix it, re-check it live. Use when the user asks for fix, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-fix

**Command:** `/webdev fix <url or brief>`

Find the fault, fix it, re-check it live.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `fix`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Reproduce the fault first; never fix a guess.
2. Fix the smallest change that solves it; back up first.
3. Re-check live and show the before/after.

## Checklist
- [ ] Fault reproduced
- [ ] Fix applied
- [ ] Live re-check passed

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
