---
name: webdev-forms
description: "Forms, validation, success/error states, spam protection, email delivery. Use when the user asks for forms, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-forms

**Command:** `/webdev forms <url or brief>`

Forms, validation, success/error states, spam protection, email delivery.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `forms`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Test every form with empty, wrong and correct input.
2. Check success and error states and where the submission goes.
3. Never claim delivery is confirmed until the owner checks the inbox.

## Checklist
- [ ] Required fields validated
- [ ] Error messages clear
- [ ] Success state shown
- [ ] Spam protection on

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
