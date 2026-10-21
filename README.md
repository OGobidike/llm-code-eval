# Python Code-Response Evaluation

A small, reproducible evaluation of how two AI models answer Python coding questions, graded the way AI-training work is graded: against a written rubric, side by side, with written rationales, gold rewrites, and a blind consistency check.

Every coding response is also **run against hidden tests**, so correctness is verified by execution, not just judged by reading.

The full plan, phase by phase, is in [`docs/BLUEPRINT.md`](docs/BLUEPRINT.md).

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

**Models:** GPT-6 (ChatGPT web, temporary chat) as model-1 and Qwen-3.7 plus
(Qwen Chat web, thinking mode off) as model-2, collected in October 2026. Full
settings are in [`responses/MODELS.md`](responses/MODELS.md); the full numbers
are in [`results/summary.md`](results/summary.md).

| | GPT-6 | Qwen-3.7 plus |
|---|---|---|
| Average overall score (1–5) | **4.61** | 4.44 |
| Side-by-side wins (9 ties) | **5** | 4 |
| Responses passing every hidden test | **100%** | 92% |
| Correctness | 4.72 | 4.72 |

**Consistency:** on the blind re-grade (five prompts, A and B swapped, a day
later), the overall score was identical for 8 of 10 responses and within one
point for all 10. The preference matched on 3 of 5 pairs; the other two moved
one step (tie versus slight) and none flipped to the other model.

**Calibration:** no response was graded correct (4–5) while failing tests, and
none was graded wrong (1–2) while passing them.

### Findings

1. **Equally correct; GPT-6 was clearer.** Both models scored 4.72 on
   correctness. GPT-6 led on code quality (4.67 vs 4.44) and explanation
   (4.67 vs 4.50); Qwen's lower scores came mostly from padding and long
   detours, such as a lecture on `math.fsum` and `Decimal` in answer to a
   one-line `sum()` question.
2. **Passing every test isn't the same as meeting the request.** On
   `merge_intervals`, both models passed all 6 hidden tests, yet both
   appended the caller's inner lists and then edited them, breaking the
   prompt's "don't modify the input" rule. Only reading the code caught it, so
   both were graded 3 for correctness. On the dict-mutation fix, Qwen's main
   answer was right, but it ended with a "new dict" alternative that broke
   "return the same dict" and failed a hidden test.
3. **Only one model handled the vague request.** Asked to "clean up phone
   numbers", Qwen pointed out the ambiguity, stated its assumptions and said
   what it returns. GPT-6 silently assumed a format and returned `None` for
   input like `"abc"` without a warning. It was Qwen's clearest win.

### Example: `merge_intervals` (impl-02)

**Prompt:** merge a list of `[start, end]` pairs given in any order; touching
intervals like `[1, 3]` and `[3, 5]` must merge; don't modify the input list.

**Both responses** sorted the intervals, merged overlapping and touching ones,
and passed all 6 hidden tests. Both also appended the caller's own inner lists
to the result and then changed them with `merged[-1][1] = ...`, so
`data = [[1, 3], [2, 6]]` becomes `[[1, 6], [2, 6]]` after the call.

**Rationale (tie):** "Both sort, merge overlapping and touching intervals, and
pass all hidden tests, but both append the caller's inner lists without
copying and then change them through merged[-1][1], breaking the prompt's rule
not to modify the input. B's comments are clearer, but neither would serve the
user better."

The [gold rewrite](gold/impl-02.md) fixes this by appending a new
`[start, end]` list, and passes the same tests.

### Limitations

- 18 prompts, two models and one grader, so these are directional findings,
  not benchmarks.
- I wrote the prompts and the tests myself, so they reflect what I chose to
  check.
- Response A won only 2 of the 9 decided pairs, which may be a lean toward
  position B; with this few pairs it could also be chance.
- For the re-grade, the checklists were written fresh and blind; the scores
  were then drafted with an AI assistant from those fresh checklists using the
  rubric anchors, and reviewed by me.

## Run it yourself

Requires Python 3.11 or later.

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash; on macOS or Linux: source .venv/bin/activate
pip install -r requirements.txt

# 1. Save each answer as responses/raw/<model>/<prompt_id>.md, then:
python scripts/collect_responses.py
# 2. Run the hidden tests (also checks your gold rewrites in gold/)
python scripts/run_tests.py
# 3. Build the blind review sheets, then grade in ratings/ratings.csv and ratings/preferences.csv
python scripts/make_review.py
python scripts/check_sheet.py amb-01   # check each graded sheet before committing it
# 4. A day later: re-grade a sample into ratings/regrade_*.csv. If the blind key is
#    outside the folder, give its path; the script reads it without showing it.
python scripts/make_regrade.py ~/blind_key.csv
# 5. Put the key back in ratings/blind_key.csv, then summarize
python scripts/summarize.py
```

`run_tests.py` executes model-written code on your machine, in a temporary folder with a time limit. Skim each response before running it.

## Layout

```
docs/           the blueprint
prompts/        the 18 prompts (prompts.jsonl, and PROMPTS.md to read)
tests/prompts/  hidden tests, one file per coding prompt
responses/      MODELS.md, raw answers (raw/<model>/<prompt_id>.md) and responses.jsonl
review/         blind review sheets, and review/regrade/
ratings/        grades, preferences, the blind key, and re-grades
gold/           ideal rewrites of the weakest responses
results/        test results and summary.md
scripts/        the pipeline
```
