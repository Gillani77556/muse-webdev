---
name: webdev-accessibility
description: "Keyboard, screen reader, contrast, focus — usable by everyone. Use when the user asks for accessibility, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-accessibility

**Command:** `/webdev accessibility <url or brief>`

Keyboard, screen reader, contrast, focus — usable by everyone.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `accessibility`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Tab through the page with the keyboard only.
2. Check focus visibility, labels, alt text and contrast.
3. Fix in order: labels, focus, contrast, then structure.

## Checklist
- [ ] Keyboard navigable
- [ ] Focus visible
- [ ] Alt text present
- [ ] Contrast 4.5:1

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
