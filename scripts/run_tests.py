"""Run each response's code against the hidden tests for its prompt.

Model-written code runs on your machine, in a temporary folder, with a time limit.
Read a response before running it if anything in it looks like it touches files or the network.

Usage: python scripts/run_tests.py
Writes results/test_results.csv.
"""
import csv
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from common import (
    RESULTS,
    extract_solution,
    function_name,
    load_prompts,
    load_responses,
    test_file_for,
)

TIME_LIMIT = 20  # seconds per response


def run_one(prompt_id, response_text):
    func = function_name(prompt_id)
    code = extract_solution(response_text, func)
    if code is None:
        return {"status": "no_code", "passed": 0, "total": 0}

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "solution.py").write_text(code, encoding="utf-8")
        shutil.copy(test_file_for(prompt_id), tmp / "test_hidden.py")
        report = tmp / "report.xml"
        try:
            subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                 f"--junitxml={report}", "test_hidden.py"],
                cwd=tmp, capture_output=True, timeout=TIME_LIMIT,
            )
        except subprocess.TimeoutExpired:
            return {"status": "timeout", "passed": 0, "total": 0}
        if not report.exists():
            return {"status": "error", "passed": 0, "total": 0}

        suite = ET.parse(report).getroot()
        suite = suite.find("testsuite") if suite.tag == "testsuites" else suite
        total = int(suite.get("tests", 0))
        failed = sum(int(suite.get(k, 0)) for k in ("failures", "errors", "skipped"))
        if total == 0:  # the solution didn't even import
            return {"status": "error", "passed": 0, "total": 0}
        passed = total - failed
        return {"status": "pass" if passed == total else "fail", "passed": passed, "total": total}


def main():
    prompts = load_prompts()
    rows = []
    for prompt_id, responses in sorted(load_responses().items()):
        if not prompts[prompt_id]["tested"]:
            continue
        for r in responses:
            result = run_one(prompt_id, r["response"])
            rows.append({"prompt_id": prompt_id, "model": r["model"], **result})
            print(f"{prompt_id:8} {r['model']:20} {result['status']:8} "
                  f"{result['passed']}/{result['total']}")

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "test_results.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt_id", "model", "status", "passed", "total"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nwrote {out.relative_to(out.parents[1])}")


if __name__ == "__main__":
    main()
