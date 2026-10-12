"""Build blind review sheets: each prompt's two responses as A and B, in random order.

Usage: python scripts/make_review.py
Writes review/<prompt_id>.md, ratings/blind_key.csv (don't open it until you've
finished grading), and blank ratings/ratings.csv and ratings/preferences.csv.
"""
import csv
import random

from common import (
    PREFERENCE_FIELDS,
    RATING_FIELDS,
    RATINGS,
    RESULTS,
    REVIEW,
    load_prompts,
    load_responses,
    write_csv_template,
)

SEED = 2026


def load_test_results():
    path = RESULTS / "test_results.csv"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return {(r["prompt_id"], r["model"]): r for r in csv.DictReader(f)}


def test_line(result):
    if result is None:
        return "_No hidden tests for this prompt: judge correctness by reading._"
    if result["status"] in ("no_code", "error", "timeout"):
        return f"**Hidden tests:** {result['status']}"
    return f"**Hidden tests:** {result['passed']}/{result['total']} passed"


def sheet(prompt, slots, tests, heading):
    lines = [f"# {heading}: {prompt['id']} ({prompt['category']})", "", "## Prompt", "",
             prompt["prompt"], ""]
    for slot, r in slots:
        lines += ["---", "", f"## Response {slot}", "",
                  test_line(tests.get((prompt["id"], r["model"]))) if prompt["tested"]
                  else test_line(None), "", r["response"], ""]
    return "\n".join(lines)


def main():
    prompts = load_prompts()
    responses = load_responses()
    tests = load_test_results()
    rng = random.Random(SEED)
    REVIEW.mkdir(exist_ok=True)
    RATINGS.mkdir(exist_ok=True)

    key_rows, rating_rows, pref_rows = [], [], []
    for prompt_id in sorted(responses):
        pair = responses[prompt_id]
        if len(pair) != 2:
            print(f"skipped {prompt_id}: needs exactly 2 responses, has {len(pair)}")
            continue
        rng.shuffle(pair)
        slots = list(zip("AB", pair))
        (REVIEW / f"{prompt_id}.md").write_text(
            sheet(prompts[prompt_id], slots, tests, "Review"), encoding="utf-8")
        for slot, r in slots:
            key_rows.append({"prompt_id": prompt_id, "slot": slot, "model": r["model"]})
            rating_rows.append({"prompt_id": prompt_id, "slot": slot})
        pref_rows.append({"prompt_id": prompt_id})

    with open(RATINGS / "blind_key.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt_id", "slot", "model"])
        writer.writeheader()
        writer.writerows(key_rows)
    write_csv_template(RATINGS / "ratings.csv", RATING_FIELDS, rating_rows)
    write_csv_template(RATINGS / "preferences.csv", PREFERENCE_FIELDS, pref_rows)
    print(f"wrote {len(pref_rows)} review sheets to review/")


if __name__ == "__main__":
    main()
