"""Check the filled-in grades and write results/summary.md.

Usage: python scripts/summarize.py
"""
import sys

import pandas as pd

from common import RATINGS, RESULTS

SCORES = ["correctness", "instruction_following", "code_quality", "explanation", "overall"]
OPTIONAL_SCORES = {"code_quality", "explanation"}  # may be blank when they don't apply
STRENGTHS = {"slight", "clear", "strong"}


def read(name):
    return pd.read_csv(RATINGS / name, dtype=str, keep_default_na=False)


def check_ratings(df, name):
    problems = []
    for _, row in df.iterrows():
        where = f"{name} {row['prompt_id']} {row['slot']}"
        for col in SCORES:
            value = row[col].strip()
            if value == "" and col in OPTIONAL_SCORES:
                continue
            if value not in {"1", "2", "3", "4", "5"}:
                problems.append(f"{where}: {col} must be 1-5, got {value!r}")
    return problems


def check_preferences(df, name):
    problems = []
    for _, row in df.iterrows():
        where = f"{name} {row['prompt_id']}"
        preferred, strength = row["preferred"].strip(), row["strength"].strip()
        if preferred not in {"A", "B", "tie"}:
            problems.append(f"{where}: preferred must be A, B or tie, got {preferred!r}")
        elif preferred != "tie" and strength not in STRENGTHS:
            problems.append(f"{where}: strength must be slight, clear or strong")
        if not row["rationale"].strip():
            problems.append(f"{where}: rationale is empty")
    return problems


def to_numbers(df):
    df = df.copy()
    for col in SCORES:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def table(df):
    """Render a DataFrame as a Markdown table."""
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, row in df.iterrows():
        cells = [("n/a" if pd.isna(v) else f"{v:.2f}") if isinstance(v, float) else str(v)
                 for v in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def main():
    key = read("blind_key.csv")
    ratings, prefs = read("ratings.csv"), read("preferences.csv")
    problems = check_ratings(ratings, "ratings.csv") + check_preferences(prefs, "preferences.csv")
    if problems:
        print("Fix these first:\n  " + "\n  ".join(problems))
        sys.exit(1)

    out = ["# Results", ""]
    ratings = to_numbers(ratings).merge(key, on=["prompt_id", "slot"])

    # Scores by model
    means = ratings.groupby("model")[SCORES].mean().reset_index()
    out += ["## Average scores (1-5)", "", table(means), ""]

    # Preferences by model
    winners = prefs.merge(key, left_on=["prompt_id", "preferred"], right_on=["prompt_id", "slot"],
                          how="left")
    wins = winners["model"].value_counts()
    ties = int((prefs["preferred"] == "tie").sum())
    win_rows = pd.DataFrame({"model": sorted(key["model"].unique())})
    win_rows["wins"] = win_rows["model"].map(wins).fillna(0).astype(int)
    out += ["## Side-by-side preferences", "", table(win_rows), "", f"Ties: {ties}", ""]
    decided = prefs[prefs["preferred"] != "tie"]
    if len(decided):
        share_a = (decided["preferred"] == "A").mean()
        out += [f"**Position check:** response A won {share_a:.0%} of decided pairs "
                "(near 50% means no position bias).", ""]

    # Hidden tests against my correctness grades
    tests_path = RESULTS / "test_results.csv"
    if tests_path.exists():
        tests = pd.read_csv(tests_path)
        # A timeout or a crash counts as a failure, not as zero tests.
        rate_rows = (tests.assign(all_passed=tests["status"] == "pass")
                     .groupby("model")["all_passed"].mean()
                     .rename("responses passing every test").reset_index())
        out += ["## Hidden tests", "", table(rate_rows), ""]
        joined = ratings.merge(tests, on=["prompt_id", "model"])
        too_kind = joined[(joined["correctness"] >= 4) & (joined["status"] != "pass")]
        too_harsh = joined[(joined["correctness"] <= 2) & (joined["status"] == "pass")]
        out += ["## Calibration: my grades against the tests", "",
                f"- Graded correct (4-5) but failed tests: {len(too_kind)}"
                + "".join(f"\n  - {r.prompt_id} {r.slot}" for r in too_kind.itertuples()),
                f"- Graded wrong (1-2) but passed every test: {len(too_harsh)}"
                + "".join(f"\n  - {r.prompt_id} {r.slot}" for r in too_harsh.itertuples()),
                "",
                "Each one deserves a note: either the tests missed something, or the grade did.",
                ""]

    # Consistency on the blind re-grade
    if (RATINGS / "regrade_ratings.csv").exists():
        re_ratings, re_prefs = read("regrade_ratings.csv"), read("regrade_preferences.csv")
        problems = (check_ratings(re_ratings, "regrade_ratings.csv")
                    + check_preferences(re_prefs, "regrade_preferences.csv"))
        if problems:
            print("Re-grade not summarized yet:\n  " + "\n  ".join(problems))
        else:
            swap = {"A": "B", "B": "A", "tie": "tie"}
            re_ratings = to_numbers(re_ratings)
            re_ratings["slot"] = re_ratings["slot"].map(swap)  # back to first-pass slots
            pair = ratings.merge(re_ratings, on=["prompt_id", "slot"], suffixes=("", "_re"))
            diff = (pair["overall"] - pair["overall_re"]).abs()
            re_prefs["preferred"] = re_prefs["preferred"].map(swap)
            same = prefs.merge(re_prefs, on="prompt_id", suffixes=("", "_re"))
            agree = (same["preferred"] == same["preferred_re"]).mean()
            out += ["## Consistency (blind re-grade, A and B swapped)", "",
                    f"- Overall score identical: {(diff == 0).mean():.0%} of {len(pair)} responses",
                    f"- Overall score within 1 point: {(diff <= 1).mean():.0%}",
                    f"- Same preference: {agree:.0%} of {len(same)} pairs", ""]

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.md").write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
