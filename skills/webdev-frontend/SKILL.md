---
name: webdev-frontend
description: "HTML/CSS/JS, Tailwind, components, clean code. Use when the user asks for frontend, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-frontend

**Command:** `/webdev frontend <url or brief>`

HTML/CSS/JS, Tailwind, components, clean code.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `frontend`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Build with clean, named components; no copy-paste duplication.
2. Check the browser console for errors on every page.
3. Keep CSS in one system; remove unused styles.

## Checklist
- [ ] Valid HTML
- [ ] No console errors
- [ ] Components reused
- [ ] No dead code

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
