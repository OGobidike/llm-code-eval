"""Check one graded sheet before you commit it.

Usage: python scripts/check_sheet.py exp-01

Lists anything that would break the summary: a missing or extra row, a score
outside 1-5, an empty rationale, a note split into extra columns, or a second
header line.
"""
import csv
import sys

from common import RATINGS
from summarize import OPTIONAL_SCORES, SCORES, STRENGTHS


def read_rows(name):
    """Return (line number, row) pairs, so problems can point at the line."""
    with open(RATINGS / name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [(reader.line_num, row) for row in reader]


def file_problems(name, rows):
    problems = []
    for line, row in rows:
        if row.get("prompt_id") == "prompt_id":
            problems.append(f"{name} line {line}: a second header line; delete it")
        if None in row:
            problems.append(f"{name} line {line}: extra columns. A comma is splitting a note or "
                            "rationale; quote the text, with no space before the opening quote")
        elif any((value or "").startswith(' "') for value in row.values()):
            problems.append(f"{name} line {line}: a space before an opening quote; "
                            "write ,\"text\" with no space after the comma")
    return problems


def sheet_problems(prompt_id):
    ratings, prefs = read_rows("ratings.csv"), read_rows("preferences.csv")
    problems = file_problems("ratings.csv", ratings) + file_problems("preferences.csv", prefs)

    mine = [row for _, row in ratings if row["prompt_id"] == prompt_id]
    slots = sorted(row["slot"] for row in mine)
    if slots != ["A", "B"]:
        problems.append(f"ratings.csv: expected one row each for A and B, found {slots or 'none'}")
    for row in mine:
        for col in SCORES:
            value = (row.get(col) or "").strip()
            if value == "" and col in OPTIONAL_SCORES:
                continue
            if value not in {"1", "2", "3", "4", "5"}:
                problems.append(f"ratings.csv {prompt_id} {row['slot']}: {col} must be 1-5, "
                                f"got {value!r}")

    pref = [row for _, row in prefs if row["prompt_id"] == prompt_id]
    if len(pref) != 1:
        problems.append(f"preferences.csv: expected one row for {prompt_id}, found {len(pref)}")
    for row in pref:
        preferred = (row.get("preferred") or "").strip()
        strength = (row.get("strength") or "").strip()
        if preferred not in {"A", "B", "tie"}:
            problems.append(f"preferences.csv {prompt_id}: preferred must be A, B or tie, "
                            f"got {preferred!r}")
        elif preferred != "tie" and strength not in STRENGTHS:
            problems.append(f"preferences.csv {prompt_id}: strength must be slight, clear "
                            "or strong")
        if not (row.get("rationale") or "").strip():
            problems.append(f"preferences.csv {prompt_id}: rationale is empty")
    return problems


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/check_sheet.py <prompt_id>, for example exp-01")
    prompt_id = sys.argv[1]
    problems = sheet_problems(prompt_id)
    if problems:
        print("Fix these first:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print(f"{prompt_id} is ready to commit.")


if __name__ == "__main__":
    main()
