#!/usr/bin/env python3
"""Requirement smell scanner — starter for the A1 defect review (section 3b).

Usage:
    python3 scripts/req_smell_check.py SRS.md

What it does (rule-based, no API key needed):
  * flags WEAK / vague words that make a requirement unverifiable
  * flags non-atomic requirements ("and/or", multiple 'shall')
  * flags requirements with no actor or no 'shall'
  * flags user stories missing Given/When/Then acceptance criteria
  * flags requirements that cite no class/method (traceability smell)

This is a STARTER. Your team must extend it into an LLM-assisted review
(LangChain): send each requirement to your LLM with a prompt asking for
ambiguity/atomicity/testability findings, then YOU judge each finding.
Record the prompt and your accept/reject decisions in AI_USAGE.md, and the
confirmed defects + fixes in docs/req-review.md. The rule-based pass below
catches the mechanical smells; the LLM pass catches the semantic ones.
"""
import re
import sys

WEAK_WORDS = [
    "fast", "quick", "quickly", "easy", "easily", "user-friendly", "efficient",
    "appropriate", "adequate", "sufficient", "reasonable", "robust", "flexible",
    "seamless", "intuitive", "etc", "and so on", "as needed", "if possible",
    "should", "could", "might", "may ", "some ", "several ", "various",
]

def is_requirement_line(line: str) -> bool:
    return bool(re.match(r"^\s*[-*]?\s*(REQ|US|NFR)-\d+", line))

def check(path: str) -> int:
    findings = []
    lines = open(path, encoding="utf-8").read().splitlines()
    for n, line in enumerate(lines, 1):
        if not is_requirement_line(line):
            continue
        low = " " + line.lower() + " "
        rid = re.match(r"^\s*[-*]?\s*((?:REQ|US|NFR)-\d+)", line).group(1)

        for w in WEAK_WORDS:
            if w in low:
                findings.append((n, rid, f"weak/vague word '{w.strip()}' — is this verifiable?"))
        if low.count(" shall ") > 1:
            findings.append((n, rid, "multiple 'shall' — non-atomic requirement? split it"))
        if " and/or " in low:
            findings.append((n, rid, "'and/or' — ambiguous; pick one or split"))
        if rid.startswith("REQ") and " shall " not in low:
            findings.append((n, rid, "no 'shall' — is this a requirement or a remark?"))
        if rid.startswith("US") and not re.search(r"given.*when.*then", low):
            findings.append((n, rid, "user story without Given/When/Then acceptance criteria"))
        if rid.startswith("REQ") and not re.search(r"\(.*[A-Z][A-Za-z]+.*\)", line):
            findings.append((n, rid, "no class/method citation — traceability smell"))

    if not findings:
        print("No mechanical smells found. Now run your LLM pass for the semantic ones.")
        return 0
    print(f"{len(findings)} candidate defect(s) — judge each one (accept/reject), do not auto-fix:\n")
    for n, rid, msg in findings:
        print(f"  line {n:>4}  {rid:<9} {msg}")
    print("\nRecord confirmed defects + fixes in docs/req-review.md; decisions in AI_USAGE.md.")
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: req_smell_check.py SRS.md"); sys.exit(2)
    sys.exit(check(sys.argv[1]))
