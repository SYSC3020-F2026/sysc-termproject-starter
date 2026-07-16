# Requirements Traceability Matrix (RTM)

*Living document. Start in Assignment 1 (requirement → use case → code). Extend each assignment with design elements (A2–A4) and tests (A5–A6). Keep it in the repo as `RTM.md`.*

**How to read a row:** each requirement has an ID (a Linear issue ID). Follow it left-to-right to the use case, the design element that realises it, the code (class/method), and the test that verifies it. Every requirement must eventually reach a test. The examples below are for the **JPacman core game logic** — replace them with your own.

| Req ID | Requirement (short) | Use case | Design element (class / seq / statechart / pattern) | Code (class / method) | Test case | Status |
|--------|---------------------|----------|-----------------------------------------------------|-----------------------|-----------|--------|
| REQ-01 | The player earns 10 points and the pellet disappears when moving onto a pellet | Consume pellet (S2.1) | Sequence: move → PlayerCollisions; PointCalculator | `level/PlayerCollisions`, `points/PointCalculator` | TC-Pellet-Consume-01 | done |
| REQ-02 | The game is over when the player and a ghost meet on a square | Player dies (S2.4) | Observer: Level → LevelObserver (level lost) | `level/PlayerCollisions`, `level/Level` | TC-Player-Dies-01 | in progress |
| REQ-03 | Clyde flees when the shortest path to the player is <= 8 squares | Ghost moves (S3.x) | Strategy/Template Method: `Ghost.nextAiMove` | `npc/ghost/Clyde#nextAiMove` (SHYNESS) | TC-Clyde-Shyness-08 | in progress |
| REQ-04 | A ghost that leaves a pellet square makes the pellet visible again | Ghost over pellet (S3.3) | Sequence: ghost move on/off a pellet square | `npc/Ghost`, `board/Square` | TC-Ghost-Pellet-Reveal-01 | not started |
| REQ-05 | The player wins once all pellets are eaten | Player wins (S2.5) | Observer: Level → LevelObserver (level won) | `level/Level#remainingPellets` | TC-Level-Won-01 | not started |
