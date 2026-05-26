#!/usr/bin/env python3
"""
generate_index.py — build compounds_to_foods.json from foods.json.

This script reads foods.json (the source of truth for which foods contain
which compounds) and produces compounds_to_foods.json (the inverted index
of compound → foods, useful for "what else has this flavor?" queries).

Run from the flavor-matrix/ directory:
    python3 generate_index.py

Optional: also validates that every compound mentioned in foods.json appears
in compound_pairings.json, and prints any orphans.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).parent
FOODS = HERE / "foods.json"
PAIRINGS = HERE / "compound_pairings.json"
INDEX = HERE / "compounds_to_foods.json"


def main() -> int:
    with FOODS.open() as f:
        foods = json.load(f)
    with PAIRINGS.open() as f:
        pairings = json.load(f)

    # Build inverted index: compound -> sorted list of {food, strength}
    inverted: dict[str, list[dict]] = defaultdict(list)
    for food_name, food_data in foods.items():
        for compound in food_data.get("compounds", []):
            inverted[compound["name"]].append(
                {"food": food_name, "strength": compound["strength"]}
            )

    # Sort: strength desc (high -> medium -> low), then alphabetical
    strength_order = {"high": 0, "medium": 1, "low": 2}
    for compound in inverted:
        inverted[compound].sort(
            key=lambda e: (strength_order.get(e["strength"], 99), e["food"])
        )

    # Write derived file (compound keys sorted alphabetically for stable diffs)
    sorted_inverted = {k: inverted[k] for k in sorted(inverted)}
    with INDEX.open("w") as f:
        json.dump(sorted_inverted, f, indent=2)
        f.write("\n")

    # Validation: compounds in foods.json but not in compound_pairings.json
    in_foods = set(inverted.keys())
    in_pairings = set(pairings.keys())
    orphans = in_foods - in_pairings
    stale = in_pairings - in_foods

    print(f"Wrote {INDEX.name} with {len(inverted)} compounds covering {len(foods)} foods.")
    if orphans:
        print(f"\nWarning: {len(orphans)} compound(s) in foods.json have no entry in compound_pairings.json:")
        for c in sorted(orphans):
            print(f"  - {c}")
    if stale:
        print(f"\nNote: {len(stale)} compound(s) in compound_pairings.json are not referenced by any food (harmless but worth pruning):")
        for c in sorted(stale):
            print(f"  - {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
