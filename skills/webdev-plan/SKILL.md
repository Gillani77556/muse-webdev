---
name: webdev-plan
description: "Turn business, audience, goal, budget and timeline into a build plan. Use when the user asks for plan, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# webdev-plan

**Command:** `/webdev plan <url or brief>`

Turn business, audience, goal, budget and timeline into a build plan.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `plan`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Read the topic and derive the plan from it with the AUTO defaults below —
   never ask questions first. Goal, audience, pages, budget and timeline come
   from the topic; anything missing is a default, not a question.
2. List pages, sections, CTAs and integrations in priority order.
3. Write the plan as a checklist the user can approve line by line.

## AUTO MODE — build from the topic alone (default)
The user only gives a topic, for example "a bakery website in Lahore". That is
enough — **build the plan immediately, do not ask questions first.** Apply
these defaults and keep going:
- Business name: descriptive name from the topic, marked `[TO CONFIRM]`.
- Audience: the obvious customer for the topic (bakery → local customers
  buying fresh bread, cakes and pastries).
- Pages: Home, Products/Services, About, FAQ, Contact. Add a shop/order page
  only if the topic is a shop.
- Phone / WhatsApp / email: omit; contact form + `[TO CONFIRM]` placeholder.
  Never invent a real-looking number or address.
- Colours: pick a professional palette from the topic.
- Prices: sample prices labelled "Sample price".
- Budget / timeline: write `[TO CONFIRM]` — never guess.
Only ask the user when a fact truly blocks the build (for example a live
domain to deploy to). List every default used so the user can correct it in
one message.

## Checklist
- [ ] Goal is written in one sentence
- [ ] Audience named
- [ ] Pages listed
- [ ] Budget and timeline stated

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
