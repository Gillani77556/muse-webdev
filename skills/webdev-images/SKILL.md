---
name: webdev-images
description: "Images, icons, OG/social images, alt text, size and format. Use when the user asks for images, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-images

**Command:** `/webdev images <url or brief>`

Images, icons, OG/social images, alt text, size and format.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `images`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Audit every image: size, format, alt text and loading.
2. Compress and resize; use modern formats where supported.
3. Create or verify the OG/social preview image for key pages.

## Checklist
- [ ] Every image has alt text
- [ ] Images compressed
- [ ] OG image exists
- [ ] No broken images


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Photos make or break a premium site. Rules are mandatory, not optional:
1. **Real photos only.** Every hero, card and section image is a real
   photograph of the topic/place. Use `images.unsplash.com` photo URLs with
   `?auto=format&fit=crop&w=1600&q=80` (hero `w=2000`, cards `w=1200`).
2. **Verify before use.** Run `curl -s -o /dev/null -w "%{http_code}"`
   on EVERY image URL and record the status. Only HTTP 200 URLs ship.
   A URL that fails is replaced, never shipped.
3. **Never placeholder images** — no placehold.co, dummyimage, grey boxes,
   or CSS-only "image" panels pretending to be photos.
4. **Every image:** descriptive alt text, `loading="lazy"` except the hero,
   `width`/`height` or aspect-ratio set to prevent layout shift.
5. **Consistent ratios:** hero 16/9, cards 16/10, place tiles 4/3. Crop with
   the `fit=crop` parameter, never stretch in CSS.
6. **OG/social image:** hero photo as `og:image` on every page.
7. Count and list every photo used, with its URL and HTTP status, in the
   final report.

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
