# Results

## Average scores (1-5)

| model | correctness | instruction_following | code_quality | explanation | overall |
|---|---|---|---|---|---|
| model-1 | 4.72 | 4.78 | 4.67 | 4.67 | 4.61 |
| model-2 | 4.72 | 4.83 | 4.44 | 4.50 | 4.44 |

## Side-by-side preferences

| model | wins |
|---|---|
| model-1 | 5 |
| model-2 | 4 |

Ties: 9

**Position check:** response A won 22% of decided pairs (near 50% means no position bias).

## Hidden tests

| model | responses passing every test |
|---|---|
| model-1 | 1.00 |
| model-2 | 0.92 |

## Calibration: my grades against the tests

- Graded correct (4-5) but failed tests: 0
- Graded wrong (1-2) but passed every test: 0

Each one deserves a note: either the tests missed something, or the grade did.

## Consistency (blind re-grade, A and B swapped)

- Overall score identical: 80% of 10 responses
- Overall score within 1 point: 100%
- Same preference: 60% of 5 pairs
