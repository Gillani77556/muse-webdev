---
name: webdev-testing
description: "Every button, link and form tested; mobile test; live verify. Use when the user asks for testing, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-testing

**Command:** `/webdev testing <url or brief>`

Every button, link and form tested; mobile test; live verify.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `testing`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Click every link and button; submit every form.
2. Test on mobile width and one real phone check if possible.
3. Report pass/fail per item, never a bare 'done'.

## Checklist
- [ ] All links 200
- [ ] All buttons work
- [ ] All forms tested
- [ ] Mobile passed

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
