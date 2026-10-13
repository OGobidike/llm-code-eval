# Blueprint: Python Code-Response Evaluation

The plan for this project, from an empty GitHub repo to a finished portfolio piece on LinkedIn. Tick each box as it's done.

**The goal:** show, with evidence, the core skills of AI-training work: grading model outputs against a rubric, choosing between two responses and explaining why, writing ideal responses, and staying consistent. Verifying code by running it is the engineer's edge on top.

**The rule that matters most:** every grade, preference, rationale and gold rewrite is your own judgment. Claude can review your rationales after you write them, but never writes the grades. That's what makes the project honest, and it's what you'll be asked about in interviews.

**Time:** about 2–3 focused days.

---

## Phase 0: Set up the repo

**Goal:** the project lives on your GitHub and runs on your machine.

- [ ] On GitHub, create an **empty, private** repo named `llm-code-eval`, with no README, `.gitignore` or license.
- [ ] Claude pushes the scaffold to it (the first commit).
- [ ] Clone it, create a virtual environment, and install the requirements.
- [ ] Read `GUIDELINES.md` end to end, and change anything you'd judge differently. It must be your rubric.
- [ ] Read `prompts/PROMPTS.md` so you know the 18 prompts before any model answers them.

**Done when:** `python scripts/collect_responses.py` runs on your machine and reports 0 responses.

## Phase 1: Collect the responses

**Goal:** 36 answers, 18 prompts × 2 models, saved exactly as written.

- [ ] Choose two models you can use for free, for example two different chat assistants. **Not Claude:** you use Claude day to day, so it's excluded to keep your chat history and memory out of the evaluation. Record each model's exact name and version, the date, and how you accessed it in `responses/MODELS.md`.
- [ ] Make the test fair. Use a **fresh chat for every prompt**, with no custom instructions, memory or personas turned on. A persona like Opy would change the answers.
- [ ] Paste each prompt from `PROMPTS.md` exactly. Don't add hints, and don't regenerate to get a better answer.
- [ ] Use the chat's **copy** button, so the code fences (```` ``` ````) come along, and save each answer as `responses/raw/<model>/<prompt_id>.md`. Use simple folder names, like `responses/raw/model-1/impl-01.md`.
- [ ] Run `python scripts/collect_responses.py`. It lists anything missing.
- [ ] Commit: "Add raw responses from two models".

**Done when:** the collector reports 36 responses and nothing missing.

## Phase 2: Run the hidden tests

**Goal:** proof of which code actually works.

- [ ] Skim each code answer first. If anything touches files, the network or your system, delete that part or mark the response as failed.
- [ ] Run `python scripts/run_tests.py`. Each coding response gets `pass`, `fail`, `timeout`, `no_code` or `error`.
- [ ] For each `no_code` or `error`, open the response and find out why: no code block, a renamed function, or a syntax error. Note it for grading. Don't fix the model's answer.
- [ ] Commit: "Run hidden tests on all responses".

**Done when:** `results/test_results.csv` has 26 rows, 13 coding prompts × 2 models.

## Phase 3: Build the blind review sheets

**Goal:** you grade without knowing which model wrote what.

- [ ] Run `python scripts/make_review.py`. It writes `review/<prompt_id>.md` with Response A and B in random order.
- [ ] **Don't open `ratings/blind_key.csv`** until Phase 6. Ideally, move it outside the repo folder until then.

**Done when:** 18 review sheets exist, plus blank `ratings/ratings.csv` and `ratings/preferences.csv`.

## Phase 4: Grade

**Goal:** a score, a preference and a rationale for every pair, following `GUIDELINES.md`.

- [ ] Work one review sheet at a time. Read the prompt, list its requirements, read both responses, check the test line, then score.
- [ ] Fill `ratings/ratings.csv`: five scores per response, 1–5. Leave code quality or explanation blank only where the guidelines allow it.
- [ ] Fill `ratings/preferences.csv` with A, B or tie, a strength, and a 2–4 sentence rationale that leads with the deciding factor.
- [ ] Use `notes` for anything surprising, like a test you think is wrong.
- [ ] After each sheet, run `python scripts/check_sheet.py <prompt_id>`. It catches a missing score, a split note or a duplicate row before you commit.
- [ ] Run `python scripts/summarize.py`. It checks all 18 sheets and lists anything invalid. While the blind key is out of the folder, it stops after the check; the full summary, with the **calibration** list, comes in Phase 6.
- [ ] Commit: "Grade all 18 pairs".

Work in blocks of about 6 sheets, with breaks. Tired grading is inconsistent grading, and the re-grade will show it.

**Done when:** the summary runs with no errors.

## Phase 5: Gold rewrites

**Goal:** show you can write the ideal answer, not just judge one.

- [ ] Pick the 5 responses with the lowest `overall` scores. If there's a tie, prefer variety: a bug fix, an explanation, the false premise.
- [ ] Write `gold/<prompt_id>.md` for each, following the gold-rewrite rules in `GUIDELINES.md`.
- [ ] Run `python scripts/run_tests.py` again. Gold rewrites of coding prompts must show `pass` in `results/gold_test_results.csv`.
- [ ] Commit: "Add gold rewrites".

**Done when:** 5 gold files, and every tested one passes.

## Phase 6: Blind re-grade (at least one day later)

**Goal:** measure your own consistency, the thing graders are hired for.

- [ ] Without looking at your first grades, run `python scripts/make_regrade.py ~/blind_key_llm-code-eval.csv`, giving the path where you keep the key. It reads the key without showing it, picks 5 prompts and swaps A and B.
- [ ] Grade `review/regrade/` into `ratings/regrade_ratings.csv` and `ratings/regrade_preferences.csv`.
- [ ] Put `blind_key.csv` back in `ratings/`, then run `python scripts/summarize.py`.
- [ ] Read `results/summary.md`. Wherever the two passes disagree, write one sentence on why. That reflection is portfolio material too.
- [ ] For each line in the **calibration** list (your grade and the hidden tests disagree), add a note in `ratings/ratings.csv` saying which one was right.
- [ ] Commit: "Add blind re-grade and summary".

**Done when:** `results/summary.md` includes the consistency section.

## Phase 7: Write it up and go public

**Goal:** a stranger understands the project in 60 seconds.

- [ ] Fill in the README's **Results** section:
  - which models, and the dates
  - 3–5 headline numbers: average overall score per model, win rate, share of responses passing every test, re-grade agreement
  - 3 findings in plain words, like "Model X fixed every bug but ignored the 'explain' requirement in 4 of 6 prompts"
  - one example: a prompt, the two responses in short, your rationale
  - **limitations:** 18 prompts, one grader, two models, prompts written by the grader
- [ ] Before going public:
  - no API keys or passwords anywhere
  - no tasks from Outlier or any other platform (all 18 prompts are original)
  - the models' terms allow sharing their outputs
- [ ] Add a license (MIT, like Morning Manna) if you want others to reuse it.
- [ ] Settings → **Change visibility → Public**.
- [ ] Commit: "Write up results".

**Done when:** the repo is public and the README's Results section is filled.

## Phase 8: Show it

**Goal:** recruiters and clients find it in the places they look.

- [ ] **GitHub:** pin `llm-code-eval` on your profile, next to Morning Manna. Add topics to the repo: `llm-evaluation`, `rlhf`, `ai-training`, `python`.
- [ ] **LinkedIn, Projects:** add a project with a one-line description, the GitHub link, and these skills: Python, LLM Evaluation, Data Annotation, pytest, pandas.
- [ ] **LinkedIn, Featured:** add the repo link, so it's the first thing people see on your profile.
- [ ] **LinkedIn post:** lead with your most interesting finding, then what you built, three numbers, the link, and a question to invite comments. Reply to comments in the first hour.
- [ ] **Upwork:** add it to your portfolio with a screenshot of `results/summary.md` and one review sheet.
- [ ] **Resume:** one bullet, for example: "Built a rubric-based, test-verified evaluation of two AI models on 18 Python tasks: blind side-by-side grading, written rationales, gold rewrites, and a blind re-grade with X% agreement."

**Done when:** the project is visible on GitHub, LinkedIn, Upwork and your resume.

---

## After this

- **Grow it:** more prompts (pandas, SQL, data-cleaning tasks), a third model, or a second grader to measure agreement between graders.
- **Reuse it:** the same pipeline can evaluate AI agents later, which ties into the November Personal Agent Protocol demo.
