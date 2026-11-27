---
name: webdev-ecommerce
description: "Shop, product page, cart, checkout, payment, orders. Use when the user asks for ecommerce, or the hub routes this work to you."
user-invocable: true
argument-hint: "[url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.2.0"
  category: webdev
---

# webdev-ecommerce

**Command:** `/webdev ecommerce <url or brief>`

Shop, product page, cart, checkout, payment, orders.

## Senior standard (25-30 years)
Think like a senior web developer who built the site by hand: first the
visitor's goal, then design, then code. Few colours, clean fonts, generous
whitespace, one style on every page. If it looks like a template or a robot
made it, it is not finished.

## When to use
- The user asks for `ecommerce`, or the `webdev` hub routes here.
- Never invent business facts: names, phones, prices, reviews and addresses
  come only from the user. Unknown facts are `[TO CONFIRM]`, never guessed.

## Steps
1. Check every product page: title, price, image, stock, description.
2. Walk cart to checkout with a test order; never spend real money.
3. Payments only with the method the user approved.

## Checklist
- [ ] Product info complete
- [ ] Cart works
- [ ] Checkout completable
- [ ] Payment only as approved

## Rules
- Back up first; change live only after the user approves.
- Title, URL and content changes need the user's explicit yes.
- After every fix, re-check live and show the evidence (status, screenshot
  or measured number). Never say "done" without a live check.
- Keep the site fast: no heavy fonts, no uncompressed images, no autoplay.
