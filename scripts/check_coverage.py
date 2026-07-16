#!/usr/bin/env python3
"""JaCoCo coverage gate for GitHub Classroom autograding (Assignments 5-6).

Reads every JaCoCo CSV report under the repo (target/site/jacoco/jacoco.csv,
produced by `mvn verify` with the jacoco-maven-plugin 'report' goal), filters
to the classes in the team's subsystem package, and checks that BOTH
instruction and branch coverage meet the threshold.

Usage:
    python scripts/check_coverage.py <package-substring> [threshold]

Example:
    python scripts/check_coverage.py creatures 0.90
"""
import csv
import glob
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_coverage.py <package-substring> [threshold]")
        return 2
    needles = [n.strip().lower() for n in sys.argv[1].split(",") if n.strip()]
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 0.90

    files = (glob.glob("**/target/site/jacoco/jacoco.csv", recursive=True)          # Maven
             + glob.glob("**/build/reports/jacoco/**/*.csv", recursive=True))        # Gradle (JPacman)
    if not files:
        print("FAIL: no jacoco.csv found. Did `mvn verify` run and produce a report?")
        return 1

    im = ic = bm = bc = 0
    classes = 0
    for f in files:
        with open(f, newline="") as fh:
            for row in csv.DictReader(fh):
                pkg = (row.get("PACKAGE", "") + "." + row.get("CLASS", "")).lower()
                if any(n in pkg for n in needles):
                    classes += 1
                    im += int(row["INSTRUCTION_MISSED"])
                    ic += int(row["INSTRUCTION_COVERED"])
                    bm += int(row["BRANCH_MISSED"])
                    bc += int(row["BRANCH_COVERED"])

    if classes == 0:
        print(f"FAIL: no classes matched scope {needles}.")
        return 1

    instr = ic / (ic + im) if (ic + im) else 1.0
    branch = bc / (bc + bm) if (bc + bm) else 1.0
    print(f"Coverage scope {needles}: {classes} classes")
    print(f"  Instruction coverage: {instr:.1%}  (target {threshold:.0%})")
    print(f"  Branch coverage:      {branch:.1%}  (target {threshold:.0%})")

    if instr >= threshold and branch >= threshold:
        print("PASS: coverage gate met.")
        return 0
    print("FAIL: coverage below threshold.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
