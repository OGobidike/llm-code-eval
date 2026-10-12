"""Build responses/responses.jsonl from plain files, so you never edit JSON by hand.

Save each model's answer, copied exactly, as responses/raw/<model>/<prompt_id>.md
(for example responses/raw/gemma-3-27b/impl-01.md), then run:
    python scripts/collect_responses.py
"""
import json

from common import RESPONSES, load_prompts

RAW = RESPONSES.parent / "raw"


def main():
    prompts = load_prompts()
    rows, missing = [], []
    models = sorted(d.name for d in RAW.iterdir() if d.is_dir()) if RAW.exists() else []
    for model in models:
        for prompt_id in prompts:
            path = RAW / model / f"{prompt_id}.md"
            if path.exists():
                rows.append({"prompt_id": prompt_id, "model": model,
                             "response": path.read_text(encoding="utf-8").strip()})
            else:
                missing.append(f"{model}/{prompt_id}.md")

    with open(RESPONSES, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} responses from {len(models)} models: {', '.join(models) or 'none'}")
    if missing:
        print("missing:\n  " + "\n  ".join(missing))


if __name__ == "__main__":
    main()
