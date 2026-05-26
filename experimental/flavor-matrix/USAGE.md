# How to use the flavor matrix

The matrix is a small JSON-backed lookup tool. This guide walks through the most useful query patterns with copy-pasteable Python snippets you can run from this folder. You can also just ask Claude to run any of them — the patterns below describe what's possible.

For data layout and schema, see `README.md`. This file is about *what you can do* with the data.

## Setup

All examples assume:

- You're in the `flavor-matrix/` directory
- `generate_index.py` has been run at least once (so `compounds_to_foods.json` is current)

Each snippet starts with:

```python
import json
from collections import defaultdict
from itertools import combinations

with open("foods.json") as f: foods = json.load(f)
with open("compound_pairings.json") as f: pairings = json.load(f)
with open("compounds_to_foods.json") as f: inverted = json.load(f)

STRENGTH = {"high": 3, "medium": 2, "low": 1}
```

---

## Question 1 — "What does food X taste like, chemically?"

Use when you want to understand the flavor sub-notes of a single ingredient.

```python
food = "tomato"
for c in foods[food]["compounds"]:
    print(f"  {c['strength']:6s} {c['name']:30s} — {c['notes']}")
```

> Tomato breaks down into methional (savory), Z-3-hexenal (green leaf), β-ionone (violet/floral), 2-isobutylthiazole (tomato-leaf), damascenone (rose/apple). Now you know tomato isn't just "tomato" — it has floral, green, and umami axes you can play with.

---

## Question 2 — "What other foods share compound X?"

Useful when you know a flavor note you want to lean into and want other ingredients that bring it.

```python
compound = "beta-ionone"
for entry in inverted[compound]:
    print(f"  {entry['strength']:6s} {entry['food']}")
```

> β-ionone (violet/raspberry): raspberry, carrot, tomato. Explains why carrot-raspberry salad and tomato-raspberry tea cake both work — same floral compound.

---

## Question 3 — "What foods pair well with food X overall?"

The full brainstorming walk: pulls X's compounds, finds other foods sharing them, ranks by combined overlap weight.

```python
target = "porcini_mushroom"
score = defaultdict(lambda: {"shared": [], "weight": 0})
for c in foods[target]["compounds"]:
    for entry in inverted.get(c["name"], []):
        f = entry["food"]
        if f == target: continue
        w = STRENGTH[c["strength"]] * STRENGTH[entry["strength"]]
        score[f]["shared"].append(c["name"])
        score[f]["weight"] += w
for f, info in sorted(score.items(), key=lambda kv: -kv[1]["weight"])[:10]:
    print(f"  {info['weight']:3d}  {f:20s}  via: {', '.join(info['shared'])}")
```

Add filters easily: `if not foods[f].get("vegetarian"): continue`, or filter by category.

---

## Question 4 — "What vegetarian foods could substitute for this meat?"

The flavor-swap query — finds plant foods that share key compounds with an animal protein.

```python
target = "beef"
score = defaultdict(lambda: {"shared": [], "weight": 0})
for c in foods[target]["compounds"]:
    for entry in inverted.get(c["name"], []):
        f = entry["food"]
        if f == target or not foods[f].get("vegetarian"): continue
        w = STRENGTH[c["strength"]] * STRENGTH[entry["strength"]]
        score[f]["shared"].append(c["name"])
        score[f]["weight"] += w
for f, info in sorted(score.items(), key=lambda kv: -kv[1]["weight"])[:8]:
    print(f"  {info['weight']:3d}  {f:20s}  via: {', '.join(info['shared'])}")
```

> For beef: miso, porcini, soy sauce, dark chocolate, coffee top the list. The "vegetarian beef" stack. Swap `"beef"` for `"chicken"`, `"salmon"`, `"anchovy"`, etc. to do the same for other proteins.

---

## Question 5 — "What's the most surprising pairing overall?"

Surfaces cross-category pairings ranked by chemical overlap. Great for "give me a wild idea" brainstorms (cakes, pasta dishes, unexpected combinations).

```python
def cat(f): return foods[f]["category"]
pairs = []
for a, b in combinations(foods, 2):
    a_c = {c["name"]: c["strength"] for c in foods[a]["compounds"]}
    b_c = {c["name"]: c["strength"] for c in foods[b]["compounds"]}
    shared = set(a_c) & set(b_c)
    if not shared or cat(a) == cat(b): continue
    w = sum(STRENGTH[a_c[c]] * STRENGTH[b_c[c]] for c in shared)
    pairs.append((w, a, b, sorted(shared)))
for w, a, b, s in sorted(pairs, reverse=True)[:15]:
    print(f"  {w:3d}  {a:20s} + {b:20s}  via {', '.join(s)}")
```

> Same-category pairings (two herbs, two fruits) get filtered out so the surprising stuff floats to the top. This is the engine behind "wild cake ideas" and "weird pasta dishes" brainstorms.

---

## Question 6 — "What does compound Y pair with?"

Look up a compound's neighbors in the pairing graph plus its example foods.

```python
compound = "linalool"
p = pairings[compound]
print(f"  flavor: {p['flavor_notes']}")
print(f"  pairs with: {', '.join(p['pairs_with'])}")
print(f"  found in (examples): {', '.join(p['shared_with_examples'])}")
```

> Linalool (floral/citrus/coriander) pairs with limonene, citral, β-ionone, vanillin, damascenone, eugenol. Found in: basil, blueberry, cardamom, cilantro, orange, peach, strawberry, thyme. Suggests endless cross-cuisine plays — blueberry-basil, cardamom-peach, thyme-orange.

---

## Asking Claude to run any of these

You don't need to run the snippets yourself. Just ask:

- "Use the matrix: what surprising pairings does saffron have?"
- "Run a vegetarian substitute query for chicken."
- "What dessert ingredients share compounds with miso?"
- "Top 10 cross-category pairings, filtered to weeknight-friendly ingredients."
- "I have leftover roasted carrots — what cake or pasta could I build from them?"

Claude will load the JSON, run the query, and translate the output into concrete dish ideas.

---

## When the matrix is wrong

The data is a starter set built from public food-chemistry literature and culinary practice. Trust it as a *generator of plausible combinations*, not as a citation.

The empirical test is always: cook the dish. If a chemistry-suggested pairing falls flat, the underlying compound entries were probably extrapolated — consider downgrading their `confidence` field (see README for conventions). If a pairing works beautifully and it's marked `low` confidence, upgrade it.

The matrix improves by use.
