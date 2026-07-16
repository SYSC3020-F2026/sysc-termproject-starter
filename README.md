# SYSC 3020 Term Project — Team Repository

Welcome. This repository is your team's home for the whole term project — an
engineering engagement on the open-source Java game **SERG-Delft/jpacman**.
You will engineer the **fixed project subset — the Pac-Man core game logic** — through requirements, design, and
testing across six assignments. Read the assignment handouts and the
**Project Overview** for full details.

## Expected repository layout

Keep your deliverables in these locations so the automatic checks can find them
(the checks are a *health signal*, not your grade — see below):

```
SRS.pdf                     # A1: your requirements document
RTM.md                      # Requirements Traceability Matrix (grows every assignment)
TEAM_CHARTER.md             # A1: team charter
AI_USAGE.md                 # AI-usage note (update every assignment)
docs/
  uml/        *.puml        # A2/A3: class, sequence, and state-machine diagrams (+ rendered images)
  design/     *.pdf         # A2: domain & interaction design doc
  arch/       *.pdf         # A3: architecture document
  adr/        ADR-*.md      # A3: Architecture Decision Records
  rfc/        RFC-*.md      # A4: detailed design & design-pattern RFC
  test/       TEST_PLAN.md  # A5: test plan
src/ or a submodule         # the buildable game code + your tests (see setup)
templates/                  # blank templates to copy from
```

## How work is submitted

- Do **all** work on **feature branches** and merge via **pull requests** that a
  teammate reviews and approves. Do not commit directly to `main`.
- Every change should reference its **Linear** issue ID.
- Tag each submission (`a1-submission`, `a2-submission`, …) and submit the PDF on
  Brightspace as instructed.

## Automatic checks (what they do and don't mean)

On every push, an **Autograding** workflow runs mechanical checks:
- **Assignments 1–4:** it only checks that the required files exist and that the
  code compiles. The *content* of your requirements and design documents is
  graded **by rubric**, by a human — the checkmarks here are just a reminder.
- **Assignments 5–6:** the checks are real — your tests must pass and your JaCoCo
  coverage must reach **90%** (instruction and branch) on the in-scope core-logic classes.

The green/red score is a **health signal**, not your grade. Your grade follows
the rubric in the course's *Evaluation Guide & Rubric*.

## Getting started

1. Build the game: `./gradlew build` (JPacman is self-contained — no companion libraries).
2. Copy the blanks you need from `templates/` into place and start Assignment 1.
