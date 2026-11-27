---
name: webdev-backend
description: "API, database, auth, admin, saving data. Use when the user asks for backend, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-backend

**Command:** `/webdev backend <url or brief>`

API, database, auth, admin, saving data.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `backend`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Describe the data model before writing code.
2. Protect admin areas; validate every input on the server.
3. Test save, load, edit and delete; record the backup plan.

## Checklist
- [ ] Data saves and loads
- [ ] Auth protects admin
- [ ] Errors handled
- [ ] Backups noted

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "ho gaya" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
