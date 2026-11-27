---
name: webdev-animation
description: "Smooth animation, hover and scroll — never slow, never too much. Use when the user asks for animation, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-animation

**Command:** `/webdev animation <url or brief>`

Smooth animation, hover and scroll — never slow, never too much.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `animation`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. List every animation; remove any that does not help the user.
2. Keep durations short and use transform/opacity only.
3. Respect prefers-reduced-motion.

## Checklist
- [ ] Animations under 300ms
- [ ] No layout shift
- [ ] Respects reduced motion
- [ ] No autoplay video

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
