"""Pick 5 prompts to grade a second time, blind, with A and B swapped.

Run it at least a day after your first pass, and don't look at your first grades.
Usage: python scripts/make_regrade.py
Writes review/regrade/<prompt_id>.md and blank ratings/regrade_*.csv files.
"""
import csv
import random

from common import (
    PREFERENCE_FIELDS,
    RATING_FIELDS,
    RATINGS,
    REVIEW,
    load_prompts,
    load_responses,
    write_csv_template,
)
from make_review import load_test_results, sheet

SEED = 7
SAMPLE_SIZE = 5


def main():
    with open(RATINGS / "blind_key.csv", encoding="utf-8") as f:
        key = {(r["prompt_id"], r["slot"]): r["model"] for r in csv.DictReader(f)}
    prompts = load_prompts()
    responses = load_responses()
    tests = load_test_results()

    prompt_ids = sorted({pid for pid, _ in key})
    sample = sorted(random.Random(SEED).sample(prompt_ids, min(SAMPLE_SIZE, len(prompt_ids))))
    out_dir = REVIEW / "regrade"
    out_dir.mkdir(parents=True, exist_ok=True)

    rating_rows, pref_rows = [], []
    for prompt_id in sample:
        by_model = {r["model"]: r for r in responses[prompt_id]}
        # Swap: the first pass's B is now A, so a position bias can't repeat itself.
        slots = [("A", by_model[key[(prompt_id, "B")]]), ("B", by_model[key[(prompt_id, "A")]])]
        (out_dir / f"{prompt_id}.md").write_text(
            sheet(prompts[prompt_id], slots, tests, "Re-grade"), encoding="utf-8")
        rating_rows += [{"prompt_id": prompt_id, "slot": s} for s in "AB"]
        pref_rows.append({"prompt_id": prompt_id})

    write_csv_template(RATINGS / "regrade_ratings.csv", RATING_FIELDS, rating_rows)
    write_csv_template(RATINGS / "regrade_preferences.csv", PREFERENCE_FIELDS, pref_rows)
    print("re-grade sample:", ", ".join(sample))


if __name__ == "__main__":
    main()
