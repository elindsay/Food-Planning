# Food Planning — Project Instructions

This project is for meal planning, recipes, grocery lists, and food-related research for Emma.

**Always read these before suggesting recipes, meal plans, snacks, or grocery lists:**

- `CLAUDE.md` (this file) — principles that don't change
- `preferences.md` — living document for evolving tastes, favorites, dislikes, and recipes that have been tried; append as new preferences come up
- `upcoming.md` — short-lived notes about travel, hosting, busy stretches, or anything else that should shape a specific upcoming week. Stale (past-dated) entries can be ignored or deleted.

**Read on demand only (opt-in, not for routine meal planning):**

- `research-notes.md` — Emma's notes on nutrition/health topics she's curious about. Read when she asks a follow-up question on a topic, or when its context would help inform a recommendation. Not needed for weekly planning.
- `experimental/` — sandbox of unvetted recipe ideas and ingredient experiments. **Do not include in the weekly Routine or default meal planning.** Read only when Emma explicitly asks for new recipe brainstorming, or says something like "look in experimental." See `experimental/README.md` for full rules.

## Health context

Emma recently had kidney stones (first incident, as of May 2026). The stone composition has not been identified yet, so dietary guidance should follow general kidney-stone-prevention principles that are safe across the common stone types (calcium oxalate, uric acid, and mixed) until more is known. If a recommendation depends on stone type, flag it and note the assumption.

General principles being followed in the meantime:
- **High hydration.** Target ~2.5–3 L of water daily; more on hot days or after exercise. Citrate-rich fluids (water with lemon or lime) are encouraged.
- **Lower sodium.** Aim under ~2,300 mg/day. Watch out for hidden sodium in sauces, broths, deli meats, breads, and restaurant food.
- **Moderate purines.** Not a strict low-purine diet, but go easy on high-purine foods: organ meats, anchovies, sardines, mackerel, mussels, and large amounts of any animal protein in one sitting.
- **Moderate animal protein.** Spread protein across the day rather than one huge serving.
- **Adequate dietary calcium with meals.** Counterintuitively, calcium from food (not supplements) helps bind oxalates in the gut. Don't strip calcium out.
- **Limit added sugar and sugary drinks**, especially sodas with fructose.

## Dietary goals, in priority order

When goals conflict, resolve in this order:

1. **Kidney stone prevention** — hydration, lower sodium, moderate purines, sensible protein. This trumps everything else for now.
2. **Vegetarian-leaning, with fish and chicken OK.** No beef, no pork. Plant-forward meals are preferred; fish and chicken are fine when they fit.
3. **Modest fat loss via reasonable eating + exercise.** Not aggressively cutting calories. Think "eat well, move, don't obsess." No crash diets, no extreme restriction.
4. **Protein for weight lifting.** Important but secondary to kidney health. Aim for solid protein (~0.7–1.0 g/lb bodyweight ballpark) spread across meals rather than mega-doses. Plant proteins, fish, chicken, eggs, Greek yogurt, cottage cheese, tofu, tempeh, legumes are the workhorses.
5. **Insulin-conscious / "obesity code"-leaning.** Generally favor whole foods over refined carbs, fewer sugar spikes, fat is not the enemy. Open to revisiting this with new research. Note: very high-fat diets can interact with stone risk depending on stone type, so don't push toward keto extremes until stone composition is known.

## Foods that are in / out

**In, freely:**
- Fish (especially salmon, cod, tilapia, trout — lower purine than the small oily fish), chicken, eggs
- Greek yogurt, cottage cheese, milk, cheese (in normal amounts) — dietary calcium is helpful
- Most vegetables, especially lower-oxalate ones: broccoli, cauliflower, cabbage, bell peppers, zucchini, mushrooms, lettuce, cucumber, green beans, peas
- Most fruits, especially citrus (lemon, lime, oranges) for natural citrate; berries, apples, melons
- Legumes (moderate purine but plant protein wins overall), tofu, tempeh, edamame
- Whole grains: oats, quinoa, brown rice, whole wheat (in moderate portions per the insulin angle)
- Olive oil, avocado, nuts and seeds (most are fine; almonds and cashews are higher oxalate — use, don't overuse)
- Herbs, spices, vinegar, lemon/lime, garlic (great for flavoring instead of salt)

**Use sparingly / be thoughtful:**
- High-oxalate foods (until stone type is known): spinach, Swiss chard, beets and beet greens, rhubarb, almonds in large amounts, cashews, peanuts in large amounts, dark chocolate, sweet potatoes — fine occasionally, not as everyday staples
- High-purine fish: anchovies, sardines, mackerel, herring, mussels — small/occasional servings
- High-sodium items: deli meats, canned soups, soy sauce (use low-sodium), pickles, processed snacks, most jarred sauces
- Caffeine and alcohol — moderate, and offset with extra water
- Added sugar, sugary drinks, fruit juice in large amounts

**Out:**
- Beef
- Pork (including bacon, ham, pork sausage)

## How to help with food planning

Emma is short on time. Default to:
- **Quick** (≤30 min active cook time) and **few dishes** (one-pot, sheet-pan, skillet, slow cooker, instant pot)
- **Reusable components** — cook once, eat across a few meals (e.g., a batch of roasted chicken, a pot of lentils, hard-boiled eggs)
- **Simple ingredient lists** — common grocery items, not specialty hunts
- **Snack ideas** built into any plan — emphasize protein + fiber, hydrating snacks (cucumber, melon, citrus), and grab-and-go options (Greek yogurt, cottage cheese with fruit, hummus + veg, hard-boiled eggs, edamame, a small handful of nuts)
- **Hydration prompts** woven in — e.g., a glass of water with lemon at meals

When proposing a meal plan, default structure unless asked otherwise:
- A few breakfast options (rotate, don't overplan)
- Lunch and dinner with overlapping ingredients to minimize shopping
- 2–3 go-to snacks
- A simple grocery list grouped by section (produce, protein, pantry, dairy)
- Rough sodium/protein notes if it'd help — but don't turn every meal into a macro spreadsheet

When suggesting a single recipe, include:
- Active time and total time
- Number of dishes / pans
- A flag if anything is notably high in sodium, purines, or oxalates and how to swap
- An easy protein-boost variation if applicable

## Weekly meal plan document

When generating a weekly meal plan as a document (e.g., in Craft via the scheduled Routine):

- Title format: `Week of [Month Day, Year]` (e.g., `Week of May 25, 2026`), with a fun emoji prepended to the title text (e.g., `🦋 Week of May 25, 2026`). Putting the emoji directly in the title is more reliable than Craft's document-icon API, which doesn't always apply.
- **Make each week feel a little new.** The overarching goal is to avoid drudgery — this should feel like a small weekly delight, not a templated form. Vary the emoji, the page theme, the cover photo, and occasionally the section separators. Don't repeat last week's combination.
- **Emoji:** Time-of-year or seasonal themes work well (🌸 🌷 🦋 in spring, 🌻 ☀️ 🍉 in summer, 🍂 🎃 🦔 in fall, ❄️ ⛄ 🌲 in winter), but it can be abstract and doesn't need to be food-related at all.
- **Theme** (Craft `--theme-id`): Lean into cozy, warm, personal themes — not corporate or minimalist-clinical. Good rotation set: `market-walks`, `honey`, `sage`, `lemonade`, `soft-spring`, `breathe`, `oasis`, `earthbound`, `leaves`, `warmer-layers`, `morning`, `golden-hour`, `start-of-the-day`, `little-world`, `floradora`. Match the theme to the season when it fits.
- **Cover photo** (Craft `--cover-url`, Unsplash search): Pick something seasonal, cozy, and aesthetic — fresh produce, citrus, herbs, wildflowers, sunlit kitchens, picnic spreads. Avoid stock-photo cliches (people pointing at clipboards, etc.). Search queries that tend to return nice results: "lemons", "fresh herbs", "wildflowers", "picnic", "summer fruit", "autumn leaves", "winter citrus".
- **Washi separators** (optional): Occasionally use `--separator washi --washi-pattern dot|wave|stripe` between major sections to add a little texture. Don't overuse — once or twice per page max.
- **Vibe check:** Cozy farmer's-market-on-Sunday-morning, not corporate-meal-planner-app. If the page looks like it could appear in a productivity SaaS demo, it's wrong.

## Guardrails

- Don't push extreme diets (strict keto, very low-carb, very low-fat, very low-calorie, aggressive fasting). Reasonable eating, not a regime.
- Don't recommend high-dose calcium supplements, vitamin C supplements above ~500 mg, or "kidney cleanse" products — flag if asked and suggest checking with a doctor.
- If a question really depends on knowing the kidney stone type (especially anything about strict oxalate restriction or strict purine restriction), say so and suggest Emma ask her doctor for the stone composition report.
- Don't moralize about food choices. If Emma wants pizza on a Friday, help make it work, don't lecture.
- Cite sources when making specific medical or nutrition claims that go beyond general guidance.

## Open questions to revisit

These would sharpen future suggestions once known. Ask in passing if a relevant moment comes up:
- Kidney stone composition (calcium oxalate, uric acid, struvite, cystine, mixed)
- Whether a doctor or dietitian has given specific dietary instructions
- Current weight / approximate protein target for lifting
- Any blood pressure, blood sugar, or other lab context worth factoring in
- Kitchen tools available (instant pot, air fryer, slow cooker, etc.)
- Typical weekly schedule — which days need the fastest meals
