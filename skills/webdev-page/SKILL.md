---
name: webdev-page
description: "Deep single-page check: HTML, headings, links, forms. Use when the user asks for page, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-page

**Command:** `/webdev page <url or brief>`

Deep single-page check: HTML, headings, links, forms.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `page`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Run page_checks.py on the URL and read the report.
2. Check headings, title, meta, links, images and forms by hand.
3. List fixes with the exact line or element.

## Checklist
- [ ] One H1
- [ ] Headings in order
- [ ] All links work
- [ ] Forms tested

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
