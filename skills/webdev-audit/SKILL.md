---
name: webdev-audit
description: "Full-site audit with a scored, prioritised report. Use when the user asks for audit, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-audit

**Command:** `/webdev audit <url or brief>`

Full-site audit with a scored, prioritised report.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `audit`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Fetch and render the homepage and every linked page.
2. Check design, speed, links, forms, content, security and SEO basics.
3. Return a score and a fix list ordered by impact, with evidence.

## Checklist
- [ ] Homepage renders
- [ ] All pages checked
- [ ] Score given
- [ ] Fixes prioritised

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
