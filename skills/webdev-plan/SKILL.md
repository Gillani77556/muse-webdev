---
name: webdev-plan
description: "Turn business, audience, goal, budget and timeline into a build plan. Use when the user asks for plan, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
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


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
The plan for every build must include the premium scope below, or the
plan is incomplete:
- **Design system:** palette (from topic), 2 fonts, tokens, hero photo
  subject, photo list (one real photo per card/section, URLs to verify).
- **Pages:** Home + one page per service/tour + About + FAQ + Contact.
- **Sections (homepage order):** header, hero, trust bar, services grid,
  how-it-works, why-choose-us, places, interactive planner, FAQ, final
  CTA, footer.
- **Interactive component:** name it (e.g. trip planner with live totals
  + WhatsApp message) and its inputs/outputs.
- **Photography:** list every photo needed with its subject; verify each
  URL returns 200 before build.
- **Checks:** page checks, broken links, schema, responsive, senior-review
  premium gate, live deploy check.
A plan that lists "Home, About, Contact" with no design system, no photos
and no interactive component is an incomplete plan — rewrite it.

- Never invent a phone number, price, review or address. Sample prices are
  always labelled "Sample price" on every price, plus one note on the page
  saying prices are samples. No invented reviews — omit that section.
- No lorem ipsum, no placeholder text, no placeholder images
  (placehold.co, dummyimage, grey boxes). If a real photo is unavailable,
  use a designed CSS gradient panel with a real heading — never a fake photo.

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
