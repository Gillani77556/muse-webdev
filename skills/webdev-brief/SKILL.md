---
name: webdev-brief
description: "Turn a client brief into a full blueprint: pages, sections, content, CTAs. Use when the user asks for brief, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-brief

**Command:** `/webdev brief <url or brief>`

Turn a client brief into a full blueprint: pages, sections, content, CTAs.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `brief`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Read the topic; list what is known and what is missing.
2. Draft the blueprint page by page with section, content and CTA, filling
   every gap with the AUTO defaults below — do not ask questions first.
3. Build from the blueprint; report the defaults used so the user can correct
   them in one message.

## AUTO MODE — build from the topic alone (default)
The user only gives a topic, for example "a bakery website in Lahore". That is
enough — **draft the blueprint immediately, do not ask questions first.**
Apply these defaults and keep going:
- Business name: descriptive name from the topic, marked `[TO CONFIRM]`.
- Pages: Home, Products/Services, About, FAQ, Contact. Add a shop/order page
  only if the topic is a shop.
- Phone / WhatsApp / email: omit; contact form + `[TO CONFIRM]` placeholder.
  Never invent a real-looking number or address.
- Colours: pick a professional palette from the topic.
- Prices: sample prices labelled "Sample price".
- Reviews: never invent them — omit the section entirely.
Only ask the user when a fact truly blocks the build (for example a live
domain to deploy to).

## Checklist
- [ ] Every page has a purpose
- [ ] Every section has content source
- [ ] CTAs named


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
The blueprint for every page must specify the premium elements below:
- Per page: hero photo subject, sections in order, one CTA per section.
- Per card: real photo subject + URL to verify, title, duration, 2-3
  highlights, sample price (labelled "Sample price"), WhatsApp CTA.
- Homepage blueprint always includes: hero, trust bar, tours grid,
  how-it-works, why-choose-us, places, planner, FAQ, final CTA, footer.
- Interactive component blueprint: inputs, live outputs, WhatsApp message
  format.
- Photo list: every photo with subject and verified URL (HTTP 200).
- Defaults used: list them all (name, phone, prices, palette) so the user
  can correct them in one message.
A blueprint without photos, planner and full sections is not a blueprint —
finish it before building.

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
