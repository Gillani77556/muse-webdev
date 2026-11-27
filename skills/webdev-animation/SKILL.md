---
name: webdev-animation
description: "Smooth animation, hover and scroll — never slow, never too much. Use when the user asks for animation, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-animation

**Command:** `/webdev animation <url or brief>`

Smooth animation, hover and scroll — never slow, never too much.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `animation`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. List every animation; remove any that does not help the user.
2. Keep durations short and use transform/opacity only.
3. Respect prefers-reduced-motion.

## Checklist
- [ ] Animations under 300ms
- [ ] No layout shift
- [ ] Respects reduced motion
- [ ] No autoplay video


## PREMIUM BUILD STANDARD (25-30 year expert, v0.2.0)
Motion must feel hand-built, never gimmicky:
1. **Reveal on scroll:** IntersectionObserver adds `.revealed` to sections
   and cards (opacity 0 → 1, translateY(16px) → 0, 500ms ease). Once only.
2. **Card hover:** translateY(-4px) + shadow lift, 200ms. Buttons: subtle
   scale/brightness on hover, visible focus ring on keyboard focus.
3. **Smooth anchors:** `scroll-behavior: smooth` + `scroll-margin-top` so
   the sticky header never covers a heading.
4. **Interactive feedback:** planner totals animate on change; FAQ accordion
   opens with a height/opacity transition; mobile nav slides, not jumps.
5. **Performance:** transform/opacity only, 200-300ms, no layout shift,
   no animation on load for above-the-fold content beyond a gentle fade.
6. **Respect `prefers-reduced-motion`:** disable reveals and smooth scroll.
7. Test on mobile: no animation may block tapping, scrolling or the
   WhatsApp button.

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
