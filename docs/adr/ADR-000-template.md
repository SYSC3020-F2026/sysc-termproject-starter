# ADR-NNN: <short decision title>

*Architecture Decision Record. One file per decision in `docs/adr/`. Number them sequentially (ADR-001, ADR-002, …). Keep each to one page.*

- **Status:** Proposed | Accepted | Superseded by ADR-XXX
- **Date:** YYYY-MM-DD
- **Deciders:** <names / roles>

## Context
What forces are at play? What problem or question does this decision address? (For a *recovered* decision, describe the situation the original authors faced, with evidence from the code.)

## Decision
The decision that was made (or that the code embodies), stated in one or two sentences.

## Consequences
The results — positive and negative. What becomes easier? What becomes harder or is now constrained?

## Evidence (code references)
Classes / files / packages that show this decision in the codebase.

---

## Example (worked)

# ADR-001: Per-ghost AI via an abstract `Ghost` with `nextAiMove()`

- **Status:** Accepted (recovered from SERG-Delft/jpacman)
- **Date:** 2026-09-18
- **Deciders:** Squad 7

### Context
Each ghost type (Blinky/Pinky/Inky/Clyde) needs its own hunting behaviour, but they share the movement machinery (move interval, board navigation).

### Decision
`Ghost` is an **abstract** NPC that defines the movement skeleton; each concrete ghost supplies its own **`nextAiMove()`**. Shared pathfinding lives in the `Navigation` utility.

### Consequences
- **+** New ghost behaviours are added by subclassing and overriding one method; shared logic is not duplicated.
- **-** Behaviour is spread across subclasses; understanding "how ghosts move" means reading `Ghost` plus each subclass.

### Evidence
`npc/Ghost`, `npc/ghost/Clyde#nextAiMove` (the `SHYNESS = 8` rule), `npc/ghost/Navigation`.
