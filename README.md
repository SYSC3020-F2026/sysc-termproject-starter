# SYSC 3020 Term Project — Starter Repository

This is the **starter** for the SYSC 3020 term project, based on the
open-source Java game **SERG-Delft/jpacman**. Every team works the same subset —
the **JPacman core game logic** (packages `board`, `level`, `npc`, `points`;
UI/sprite out of scope). Read the assignment handout and the **Project Overview**
on Brightspace for full details.

## What's inside

- `src/…` — the JPacman game code (read it and build it).
- `scripts/llm_req_review.py` — the LangChain reviewer skeleton you complete.
- `TEAM_CHARTER.md`, `AI_USAGE.md` — templates to fill in.
- `templates/` — blank templates to copy from.
- `doc/scenarios.md` — the game's expected behaviour.

## How to use it

**Clone this repository or download it as a ZIP**, and put the code in your
**team's own GitHub repository**; you work and commit there. What to submit,
and where, is given in **each assignment handout** on Brightspace.

## Building the game

```
./gradlew test                    # compile and run all tests — needs JDK 11
./gradlew test jacocoTestReport   # also writes the coverage report
```

On Windows, use `gradlew.bat` instead of `./gradlew`.
`./gradlew build` also runs Checkstyle, PMD and SpotBugs; use it only when an
assignment asks for static analysis.

JPacman is self-contained (no companion libraries). If the build fails, first
check that you are on **JDK 11**.
