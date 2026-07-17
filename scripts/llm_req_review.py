#!/usr/bin/env python3
"""LLM-assisted requirement review — LangChain SKELETON (you complete it).

This is the part of Assignment 1 (section 3b) where YOU build the AI reviewer.
The rule-based scanner (req_smell_check.py) catches mechanical smells; this
script must catch the SEMANTIC ones: hidden ambiguity, untestable claims,
non-atomic behaviour the rules miss, and contradictions BETWEEN requirements.

Setup (once):
    python3 -m pip install langchain langchain-openai        # or your provider's package
    export OPENAI_API_KEY=...                                # or your provider's key

Run:
    python3 scripts/llm_req_review.py SRS.md > docs/llm-review-output.md

What you must do (the graded part):
  1. Complete the PROMPT — this is prompt engineering: tell the model exactly
     what counts as a defect (use the ISO 29148 characteristics: unambiguous,
     complete, consistent, verifiable, singular, feasible, traceable), what to
     ignore, and the exact output format you want back.
  2. Complete the model call where marked TODO.
  3. Run it, then JUDGE each finding: accept or reject, with a reason.
     - confirmed defects + fixes  -> docs/req-review.md
     - the prompt + your accept/reject decisions -> AI_USAGE.md
  The tool proposes; you decide. Submitting raw LLM output as your review
  scores zero for this item.
"""
import sys

# ---------------------------------------------------------------------------
# 1. THE PROMPT — complete it. What you write here is the assignment.
# ---------------------------------------------------------------------------
PROMPT = """You are a requirements-quality reviewer for a Software Requirements
Specification (SRS) of a Pac-Man game's core logic.

Review the requirements below for defects. A defect is a violation of one of
the ISO 29148 quality characteristics:
- TODO: list the characteristics and define, in one line each, what a
        violation looks like (do not just name them).
- TODO: tell the model what NOT to flag (style preferences, formatting, ...).
- TODO: ask for cross-requirement checks (contradictions, duplicates).

For each defect found, output exactly one line:
  <REQ-ID> | <characteristic violated> | <one-sentence explanation> | <suggested fix>

If a requirement is clean, do not mention it.

Requirements:
{requirements}
"""

def load_requirements(path: str) -> str:
    """Extract requirement lines from SRS.md or a Requirement Yogi CSV export."""
    if path.lower().endswith(".csv"):
        import csv, re
        reqs = []
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for row in csv.reader(fh):
                key = next((c.strip() for c in row
                            if re.match(r"^(REQ|US|NFR)-\d+$", c.strip())), None)
                if key:
                    reqs.append(key + ". " + " ".join(c.strip() for c in row if c.strip() != key))
    else:
        lines = open(path, encoding="utf-8").read().splitlines()
        reqs = [l for l in lines if l.strip().lstrip("-* ").startswith(("REQ-", "US-", "NFR-"))]
    if not reqs:
        sys.exit("No requirement lines (REQ-/US-/NFR-) found in " + path)
    return "\n".join(reqs)

def review(path: str) -> None:
    requirements = load_requirements(path)
    prompt = PROMPT.format(requirements=requirements)

    # -----------------------------------------------------------------------
    # 2. THE MODEL CALL — complete it (LangChain).
    # -----------------------------------------------------------------------
    # TODO: something like
    #   from langchain_openai import ChatOpenAI
    #   model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    #   response = model.invoke(prompt)
    #   print(response.content)
    # Any provider works (langchain-anthropic, langchain-ollama, ...);
    # temperature 0 keeps the review reproducible.
    raise NotImplementedError(
        "Complete the PROMPT above and the model call here, then re-run. "
        "See the module docstring for what is graded."
    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: llm_req_review.py SRS.md"); sys.exit(2)
    review(sys.argv[1])
