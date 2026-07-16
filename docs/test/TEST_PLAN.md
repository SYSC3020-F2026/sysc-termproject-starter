# Test Plan — <subsystem name>

*Deliverable of Sprint 5 (extended in Sprint 6). Commit to `docs/test/`.*

## 1. Scope & objectives
What is being tested (your subsystem) and the goal (verify behaviour against the SRS/scenarios; reach the coverage gate on the core-logic packages (board/level/npc)).

## 2. Items under test
List the classes/units in scope (e.g., a ghost's `nextAiMove()`, `Navigation.shortestPath`, `PlayerCollisions`, the scoring rules) and what is explicitly **out** of scope (e.g., rendering/theming).

## 3. Test levels & approach
- **Unit** — isolate each unit with **stubs/mocks** (Lecture 10) for its dependencies.
- **Integration** — at least one end-to-end flow across component boundaries (player move → PlayerCollisions → Level outcome).
- **Acceptance** — verify the Given/When/Then acceptance criteria from the SRS.
- **Techniques** — equivalence partitioning, boundary-value analysis; structural coverage (JaCoCo) to drive additional unit cases.

## 4. Entry / exit criteria
- **Entry:** code builds; CI runs tests on PRs.
- **Exit:** all planned cases executed; **≥ 90% instruction and branch coverage** on units under test; no open high-severity SonarCloud issues; acceptance tests pass.

## 5. Environment & tools
Java + Maven; JaCoCo (coverage); SonarCloud (static analysis / quality gate); GitHub Actions (CI); (optional) PIT (mutation testing).

## 6. Risks
e.g., logic entangled with rendering (hard to isolate), timing/frame-rate dependence, randomness in ghost behaviour — and how you mitigate each.

## 7. Test cases
| ID | Level | Requirement (RTM) | Technique | Test data / preconditions | Expected result | Actual | Status |
|----|-------|-------------------|-----------|---------------------------|-----------------|--------|--------|
| TC-Pinky-Target-01 | Unit | GHO-13 | BVA | Pac-Man at (10,20) facing RIGHT | Pinky target = tile 4 ahead = (14,20) | | |
| TC-Energizer-Frighten-01 | Integration | GHO-15 | Scenario | Energizer eaten while ghosts CHASING | All ghosts transition to FRIGHTENED | | |
| TC-AttackWave-Timeout-01 | Unit | GHO-14 | Boundary | Scatter timer at its level-1 limit | Transition SCATTER → CHASE | | |

## 8. Defect log (Sprint 6)
| Defect | Found by (test / SonarCloud) | Why it is a fault | Suggested fix | Linear issue |
|--------|------------------------------|-------------------|---------------|--------------|
|  |  |  |  |  |
