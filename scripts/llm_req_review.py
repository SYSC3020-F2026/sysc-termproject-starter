#!/usr/bin/env python3
"""LLM-assisted requirement review — LangChain SKELETON (you complete it).

Task C of Assignment 1: YOU build the AI reviewer. A human checklist catches the
obvious problems; this script must catch the SEMANTIC ones — hidden ambiguity,
untestable claims, non-atomic behaviour, and contradictions BETWEEN requirements.

Setup (once) — free, local, no API key:
    # macOS
    brew install ollama && brew services start ollama
    ollama pull llama3.2
    python3 -m venv .venv
    .venv/bin/pip install langchain langchain-ollama
    # Windows (PowerShell):
    #   winget install Ollama.Ollama
    #   ollama pull llama3.2
    #   py -m venv .venv
    #   .venv\\Scripts\\pip install langchain langchain-ollama

Run:
    .venv/bin/python scripts/llm_req_review.py requirements.csv > review-output.md

What you must do (the graded part):
  1. Complete the PROMPT — prompt engineering: tell the model exactly what counts
     as a defect (ISO/IEC/IEEE 29148: unambiguous, complete, consistent,
     verifiable, singular, feasible, traceable), what to ignore, and the exact
     output format you want back.
  2. Complete the model call where marked TODO (use ChatOllama).
  3. Run it, then JUDGE each finding: accept or reject with a one-line reason.
     Record the confirmed defects, your prompt, and your accept/reject decisions
     in the DEFECT-REVIEW section of your SRS.
  The tool proposes; you decide. Submitting raw LLM output as your review
  receives no credit.
"""
import sys

# ---------------------------------------------------------------------------
# 1. THE PROMPT — complete it. What you write here is the assignment.
# ---------------------------------------------------------------------------
PROMPT = """You are a requirements-quality reviewer for a Software Requirements
Specification (SRS) of a Pac-Man game's core logic.

Review the requirements below for defects. A defect is a violation of one of
the ISO/IEC/IEEE 29148 quality characteristics:
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
    """Extract requirement lines from an SRS text file or a Requirement Yogi CSV export."""
    if path.lower().endswith(".csv"):
        import csv, re
        reqs = []
        with open(path, newline="", encoding="utf-8-sig") as fh:
            for row in csv.reader(fh):
                key = next((c.strip() for c in row
                            if re.match(r"^[A-Z][A-Z0-9]{1,9}-\d+$", c.strip())), None)
                if key:
                    reqs.append(key + ". " + " ".join(c.strip() for c in row if c.strip() != key))
    else:
        import re as _re
        lines = open(path, encoding="utf-8").read().splitlines()
        reqs = [l for l in lines if _re.match(r"^[A-Z][A-Z0-9]{1,9}-\d+", l.strip().lstrip("-* "))]
    if not reqs:
        sys.exit("No requirement lines (e.g., SJC-001) found in " + path)
    return "\n".join(reqs)

def review(path: str) -> None:
    requirements = load_requirements(path)
    prompt = PROMPT.format(requirements=requirements)

    # -----------------------------------------------------------------------
    # 2. THE MODEL CALL — complete it (LangChain + local Ollama).
    # -----------------------------------------------------------------------
    # TODO: something like
    #   from langchain_ollama import ChatOllama
    #   model = ChatOllama(model="llama3.2", temperature=0)  # temp 0 = reproducible
    #   print(model.invoke(prompt).content)
    raise NotImplementedError(
        "Complete the PROMPT above and the model call here, then re-run. "
        "See the module docstring for what is graded."
    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: llm_req_review.py requirements.csv"); sys.exit(2)
    review(sys.argv[1])
