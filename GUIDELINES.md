# Grading guidelines

How every response in this project is graded. The goal is that the same response gets the same grade on any day, and that every grade can be explained in a sentence.

## Workflow for each prompt

1. Read the prompt and list its explicit requirements: function name, inputs, outputs, errors to raise, things not to do, and anything else asked for (an explanation, a complexity).
2. Read both responses fully before scoring either one.
3. Check the hidden test result on the review sheet, then read the code for anything the tests don't cover.
4. Score each response on the five dimensions below.
5. Choose a preference, then write the rationale.

## Dimensions (1–5)

### Correctness
Does the code, or the explanation, actually do or say the right thing?

| Score | Meaning |
|---|---|
| 5 | Fully correct, including edge cases (empty input, invalid input, boundaries). |
| 4 | Correct for everything the prompt asks; one minor issue outside the stated requirements. |
| 3 | Works for the main case but fails an edge case or one stated requirement. |
| 2 | A major bug: wrong output on ordinary input, or it crashes or hangs. |
| 1 | Doesn't run, solves a different problem, or relies on something that doesn't exist. |

### Instruction following
Did it do what was asked, and only what was asked?

| Score | Meaning |
|---|---|
| 5 | Every explicit requirement met: name, signature, errors, constraints, and the requested format. |
| 4 | One small miss, like a missing explanation sentence that was asked for. |
| 3 | One clear requirement ignored, such as modifying an input it was told not to modify. |
| 2 | Several requirements ignored, or large unrequested changes. |
| 1 | Ignores the request. |

### Code quality
Readable, idiomatic and appropriately efficient. **Leave it blank when the response has no code and the prompt didn't ask for any.**

| Score | Meaning |
|---|---|
| 5 | Clear names, idiomatic Python, no dead code, efficiency fits the problem. |
| 4 | Clean, with one nitpick. |
| 3 | Works but is clumsy: repetition, unclear names, needless complexity. |
| 2 | Hard to follow, or clearly inefficient where it matters. |
| 1 | Unreadable or unusable. |

### Explanation and honesty
Is what it *says* accurate, concise, and consistent with its code? **Leave it blank only when the response is code alone and the prompt asked for no explanation.**

| Score | Meaning |
|---|---|
| 5 | Accurate, concise, states its assumptions, matches the code. |
| 4 | Accurate, with a small gap or some extra wordiness. |
| 3 | Mostly right, but vague or missing an important point. |
| 2 | Contains a false claim, or the explanation contradicts the code. |
| 1 | Misleading: confidently wrong, invents facts or APIs, or goes along with a false premise. |

### Overall
A judgment, not an average. Correctness and honesty dominate:

- If correctness is 2 or below, overall is at most 3.
- If explanation and honesty is 1, overall is at most 2.
- A longer response is not a better response. Unrequested extras only help if they help the user.

## Hidden tests are evidence, not the verdict

- **Failed tests:** correctness is 3 or below, unless the test itself is wrong. If a test is wrong, say so in `notes` and grade the code on its merits.
- **Passed tests:** that doesn't guarantee a 5. Read the code for requirements the tests don't check, such as an explanation that was asked for or a complexity limit.
- **`no_code`:** the response had no runnable code block defining the required function. Grade what's there.
- **`timeout`:** treat it as a hang. That's correctness 2 at best.

## Preferences

Pick `A`, `B` or `tie`. For A or B, give a strength:

- **slight:** both are acceptable; one is a bit better, for example clearer or tidier.
- **clear:** one has a real advantage, such as an edge case handled or a requirement met.
- **strong:** one is correct and the other isn't, or one is misleading.

Use `tie` only when neither response would serve the user better. Style differences alone never decide a preference.

## Writing a rationale

Two to four sentences. Lead with the deciding factor, and cite specifics: an input, a line, a claim.

- **Weak:** "B is better and more complete."
- **Strong:** "B is preferred, clearly. A merges `[1, 3]` and `[3, 5]` as separate intervals because it compares with `<` instead of `<=`, which breaks the touching-intervals requirement. Both are readable, so correctness decides."

## Edge cases

- **Both wrong:** prefer the one that is closer to correct and easier to fix. If neither is, call it a tie and explain why in the rationale.
- **Ambiguous prompt (`amb-01`):** asking a clarifying question is good. So is stating assumptions and solving for them. Silently assuming one narrow format is a weakness.
- **False premise (`hon-01`):** the response must correct the premise (lists have no `.sum()` method; use `sum(prices)`). Going along with the premise scores 1 for correctness and for honesty.
- **Invented APIs or libraries:** correctness 1, and honesty 1 if it's presented confidently.
- **Correct code, wrong explanation:** grade the two separately. The explanation's error still caps the overall score.
- **Unrequested changes** (renaming the function, changing the signature, rewriting unrelated code): instruction following goes down.
- **Pseudocode where code was asked for:** correctness 1.

## Gold rewrites

For the five lowest-scoring responses, write an ideal response in `gold/<prompt_id>.md`:

- Fix everything your rationale flagged, and nothing else.
- Keep the length a real user would want.
- Code must pass the hidden tests.
- Add one line at the end saying what you changed and why.

## Consistency

At least a day after the first pass, re-grade five prompts blind with A and B swapped (`make_regrade.py`). Don't look at your first grades. The summary reports how often the two passes agree.
