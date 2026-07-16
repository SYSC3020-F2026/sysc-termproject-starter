#!/usr/bin/env python3
"""Mechanical presence check for GitHub Classroom autograding.

Usage:
    python scripts/check_files.py <path> [<path> ...]

Passes (exit 0) only if EVERY given path exists and is non-empty.
Glob patterns are allowed (e.g. 'docs/*.puml'); a pattern passes if it
matches at least one non-empty file. Prints a short report either way.
"""
import glob
import os
import sys


def nonempty(path: str) -> bool:
    return os.path.isfile(path) and os.path.getsize(path) > 0


def check(pattern: str) -> bool:
    if any(ch in pattern for ch in "*?[]"):
        matches = [m for m in glob.glob(pattern, recursive=True) if nonempty(m)]
        ok = len(matches) > 0
        print(f"  {'OK ' if ok else 'MISS'}  {pattern}  "
              f"({len(matches)} match{'es' if len(matches) != 1 else ''})")
        return ok
    ok = nonempty(pattern)
    print(f"  {'OK ' if ok else 'MISS'}  {pattern}")
    return ok


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: check_files.py <path> [<path> ...]")
        return 2
    print("Presence check:")
    results = [check(p) for p in sys.argv[1:]]
    if all(results):
        print("PASS: all required files present.")
        return 0
    print("FAIL: missing required file(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
