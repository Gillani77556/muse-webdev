---
name: webdev-integrations
description: "WhatsApp, email, GA4, Maps, payment, social. Use when the user asks for integrations, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-integrations

**Command:** `/webdev integrations <url or brief>`

WhatsApp, email, GA4, Maps, payment, social.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `integrations`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. List integrations the user approved; test each one live.
2. Never paste keys or secrets in chat; use the secure store.
3. Record what happens if an integration is down.

## Checklist
- [ ] Each integration tested live
- [ ] Keys never in chat
- [ ] Fallback if service down

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
