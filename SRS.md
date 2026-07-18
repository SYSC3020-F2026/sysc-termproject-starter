# SRS - JPacman Core Game Logic

## B1. Introduction & scope
Core game logic (board, level, npc, points); ui/sprite out of scope.

## B3. Functional requirements
- REQ-001. When the player moves onto a square containing a pellet, the system shall add the pellet value to the score and remove the pellet. (PlayerCollisions.playerVersusPellet, PointCalculator)
- REQ-002. When the player and a ghost occupy the same square, the system shall kill the player and end the level as lost. (PlayerCollisions.playerVersusGhost, LevelObserver.levelLost)
- REQ-010. (code-only) While the shortest path to the player is 8 squares or fewer, Clyde shall move away from the player; otherwise it shall chase. (Clyde.nextAiMove, SHYNESS)
