"""Shared paths and loaders for the evaluation scripts."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts" / "prompts.jsonl"
RESPONSES = ROOT / "responses" / "responses.jsonl"
PROMPT_TESTS = ROOT / "tests" / "prompts"
REVIEW = ROOT / "review"
RATINGS = ROOT / "ratings"
RESULTS = ROOT / "results"

RATING_FIELDS = [
    "prompt_id", "slot", "correctness", "instruction_following",
    "code_quality", "explanation", "overall", "notes",
]
PREFERENCE_FIELDS = ["prompt_id", "preferred", "strength", "rationale"]

CODE_BLOCK = re.compile(r"```(?:python|py)?[ \t]*\n(.*?)```", re.DOTALL)


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_prompts():
    return {p["id"]: p for p in read_jsonl(PROMPTS)}


def load_responses():
    """Return {prompt_id: [response, ...]} from responses/responses.jsonl."""
    by_prompt = {}
    for r in read_jsonl(RESPONSES):
        by_prompt.setdefault(r["prompt_id"], []).append(r)
    return by_prompt


def test_file_for(prompt_id):
    return PROMPT_TESTS / f"test_{prompt_id.replace('-', '_')}.py"


def function_name(prompt_id):
    """The function the hidden tests import, read from their import line."""
    text = test_file_for(prompt_id).read_text(encoding="utf-8")
    return re.search(r"from solution import (\w+)", text).group(1)


def extract_solution(response_text, func):
    """Pick the last code block that defines `func`, or None if there isn't one."""
    blocks = [b for b in CODE_BLOCK.findall(response_text) if re.search(rf"def {func}\s*\(", b)]
    return blocks[-1] if blocks else None


def write_csv_template(path, fields, rows):
    """Write a CSV with the given rows, unless the file already exists."""
    if path.exists():
        print(f"kept existing {path.relative_to(ROOT)}")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path.relative_to(ROOT)}")
