---
name: webdev-deploy
description: "Vercel/Hostinger deploy, domain, SSL, 404, redirects. Use when the user asks for deploy, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-deploy

**Command:** `/webdev deploy <url or brief>`

Vercel/Hostinger deploy, domain, SSL, 404, redirects.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `deploy`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Deploy, then check the live URL, SSL and domain.
2. Check 404 page, redirects and that old links still work.
3. Record the live URL and deployment ID.

## Checklist
- [ ] Deploy 200
- [ ] SSL on
- [ ] Domain correct
- [ ] 404 page exists

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
