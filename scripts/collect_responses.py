"""Build responses/responses.jsonl from plain files, so you never edit JSON by hand.

Save each model's answer, copied exactly, as responses/raw/<model>/<prompt_id>.md
(for example responses/raw/gemma-3-27b/impl-01.md), then run:
    python scripts/collect_responses.py
"""
import json

from common import RESPONSES, load_prompts

RAW = RESPONSES.parent / "raw"


def looks_like_prompt(text, prompt):
    """True when the saved file is the prompt itself, not the model's answer."""
    def norm(s):
        return " ".join(s.split())
    return norm(text).startswith(norm(prompt)[:60])


def main():
    prompts = load_prompts()
    rows, missing, suspicious = [], [], []
    models = sorted(d.name for d in RAW.iterdir() if d.is_dir()) if RAW.exists() else []
    for model in models:
        for prompt_id in prompts:
            path = RAW / model / f"{prompt_id}.md"
            if path.exists():
                text = path.read_text(encoding="utf-8").strip()
                if not text or looks_like_prompt(text, prompts[prompt_id]["prompt"]):
                    suspicious.append(f"{model}/{prompt_id}.md")
                rows.append({"prompt_id": prompt_id, "model": model, "response": text})
            else:
                missing.append(f"{model}/{prompt_id}.md")

    with open(RESPONSES, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} responses from {len(models)} models: {', '.join(models) or 'none'}")
    if missing:
        print("missing:\n  " + "\n  ".join(missing))
    if suspicious:
        print("WARNING: these files are empty or hold the prompt, not the answer:\n  "
              + "\n  ".join(suspicious))


if __name__ == "__main__":
    main()
