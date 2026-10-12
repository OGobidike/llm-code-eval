# Python Code-Response Evaluation

A small, reproducible evaluation of how two AI models answer Python coding questions, graded the way AI-training work is graded: against a written rubric, side by side, with written rationales, gold rewrites, and a blind consistency check.

Every coding response is also **run against hidden tests**, so correctness is verified by execution, not just judged by reading.

## What it covers

| Skill | Where it shows |
|---|---|
| Rubric-based grading | `GUIDELINES.md`, `ratings/ratings.csv` |
| Side-by-side preference with rationales (RLHF-style) | `ratings/preferences.csv` |
| Writing ideal responses (SFT-style) | `gold/` |
| Verifying code by running it | `tests/prompts/`, `results/test_results.csv` |
| Calibration and consistency | `results/summary.md` |
| Python and pandas | `scripts/` |

## The prompt set

18 original prompts (`prompts/PROMPTS.md`), written for this project:

- **Implement (6):** chunking, merging intervals, anagrams, the longest unique substring, duration parsing, flattening.
- **Bug fix (5):** an empty-list crash, a mutable default argument, a binary search that never ends, mutating a dict while iterating, order-losing dedupe.
- **Refactor (2):** behavior must not change.
- **Explain (3):** `.sort()` vs `sorted()`, time complexity, `is` vs `==`.
- **Ambiguous (1) and false premise (1):** does the model ask, state its assumptions, and correct a wrong premise?

13 prompts have hidden pytest suites. Each bug-fix suite fails on the original buggy code, and each refactor suite passes on the original, so the tests measure what they claim to.

## Method

1. Each prompt goes to two models in a fresh chat. The answers are saved verbatim.
2. `run_tests.py` runs every code answer against its hidden tests, with a time limit.
3. `make_review.py` puts each pair on a review sheet as Response A and B in random order, so the grader doesn't know which model wrote which.
4. Every response is scored 1–5 on correctness, instruction following, code quality, and explanation and honesty, plus an overall score, following `GUIDELINES.md`.
5. Each pair gets a preference (A, B or tie), a strength, and a written rationale.
6. The five weakest responses get gold rewrites.
7. A day later, five prompts are re-graded blind with A and B swapped.
8. `summarize.py` reports scores, win rates, test pass rates, disagreements between grades and tests, position bias, and re-grade agreement.

## Results

_Filled in after grading: models compared, dates, and the key findings from `results/summary.md`._

## Run it yourself

Requires Python 3.11 or later.

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; on macOS or Linux: source .venv/bin/activate
pip install -r requirements.txt

# 1. Save each answer as responses/raw/<model>/<prompt_id>.md, then:
python scripts/collect_responses.py
# 2. Run the hidden tests
python scripts/run_tests.py
# 3. Build the blind review sheets, then grade in ratings/ratings.csv and ratings/preferences.csv
python scripts/make_review.py
# 4. A day later: re-grade the sample in ratings/regrade_*.csv
python scripts/make_regrade.py
# 5. Summarize
python scripts/summarize.py
```

`run_tests.py` executes model-written code on your machine, in a temporary folder with a time limit. Skim each response before running it.

## Layout

```
prompts/        the 18 prompts (prompts.jsonl, and PROMPTS.md to read)
tests/prompts/  hidden tests, one file per coding prompt
responses/      raw answers (raw/<model>/<prompt_id>.md) and responses.jsonl
review/         blind review sheets, and review/regrade/
ratings/        grades, preferences, the blind key, and re-grades
gold/           ideal rewrites of the weakest responses
results/        test results and summary.md
scripts/        the pipeline
```
