# Task A — Map of the JPacman core

## board
| Class | File path | Responsibility (one line) | Key methods |
|-------|-----------|---------------------------|-------------|
| Board | src/main/java/nl/tudelft/jpacman/board/Board.java | 2D grid of Squares | squareAt, getWidth, withinBorders |
| Square | src/main/java/nl/tudelft/jpacman/board/Square.java | One cell; holds Units, links to neighbours | getSquareAt, isAccessibleTo, getOccupants |
| Unit | src/main/java/nl/tudelft/jpacman/board/Unit.java | Anything placed on the board | occupy, leaveSquare, getSquare |
| Direction | src/main/java/nl/tudelft/jpacman/board/Direction.java | N/E/S/W with (dx,dy) delta | getDeltaX, getDeltaY |
| BoardFactory | src/main/java/nl/tudelft/jpacman/board/BoardFactory.java | Builds a Board of ground/wall squares | createBoard, createGround, createWall |

## level
| Class | File path | Responsibility (one line) | Key methods |
|-------|-----------|---------------------------|-------------|
| Level | src/main/java/nl/tudelft/jpacman/level/Level.java | The running level: board + players + NPCs | move, remainingPellets, isAnyPlayerAlive, start, stop |
| LevelObserver | src/main/java/nl/tudelft/jpacman/level/Level.java | Callback for level outcome | levelWon, levelLost |
| Player | src/main/java/nl/tudelft/jpacman/level/Player.java | The Pac-Man unit | getScore, addPoints, isAlive |
| Pellet | src/main/java/nl/tudelft/jpacman/level/Pellet.java | A unit worth points | getValue |
| MapParser | src/main/java/nl/tudelft/jpacman/level/MapParser.java | Text map -> Board + Units | parseMap |
| PlayerCollisions | src/main/java/nl/tudelft/jpacman/level/PlayerCollisions.java | Resolves unit collisions | collide, playerVersusGhost, playerVersusPellet |
| LevelFactory | src/main/java/nl/tudelft/jpacman/level/LevelFactory.java | Creates Level, Pellets, ghost NPCs | createLevel, createGhost, createPellet |

## npc / npc.ghost
| Class | File path | Responsibility (one line) | Key methods |
|-------|-----------|---------------------------|-------------|
| Ghost | src/main/java/nl/tudelft/jpacman/npc/Ghost.java | Abstract AI ghost (a Unit) | nextAiMove, getInterval |
| Blinky | src/main/java/nl/tudelft/jpacman/npc/ghost/Blinky.java | Chases the player's current square | nextAiMove |
| Pinky | src/main/java/nl/tudelft/jpacman/npc/ghost/Pinky.java | Targets ahead of the player | nextAiMove |
| Inky | src/main/java/nl/tudelft/jpacman/npc/ghost/Inky.java | Targets using Blinky + player positions | nextAiMove |
| Clyde | src/main/java/nl/tudelft/jpacman/npc/ghost/Clyde.java | Chases when far; flees when path <= SHYNESS (8) | nextAiMove |
| Navigation | src/main/java/nl/tudelft/jpacman/npc/ghost/Navigation.java | Path-finding utility for ghosts | shortestPath, findNearest |
| GhostFactory | src/main/java/nl/tudelft/jpacman/npc/ghost/GhostFactory.java | Creates the four ghosts | createBlinky, createPinky, createInky, createClyde |

## points
| Class | File path | Responsibility (one line) | Key methods |
|-------|-----------|---------------------------|-------------|
| PointCalculator | src/main/java/nl/tudelft/jpacman/points/PointCalculator.java | Scoring rules (interface) | collidedWithAPellet, collidedWithAGhost |
| DefaultPointCalculator | src/main/java/nl/tudelft/jpacman/points/DefaultPointCalculator.java | Adds pellet value to the score | collidedWithAPellet |
| PointCalculatorLoader | src/main/java/nl/tudelft/jpacman/points/PointCalculatorLoader.java | Loads the calculator implementation | load |

## Core events
1. Player moves onto a pellet -> score += value, pellet removed (PlayerCollisions.playerVersusPellet -> PointCalculator).
2. Player and ghost share a square -> player dies, level lost (PlayerCollisions.playerVersusGhost -> LevelObserver.levelLost).
3. Last pellet eaten -> level won (Level.remainingPellets == 0 -> LevelObserver.levelWon).
4. Ghost AI tick -> nextAiMove picks a Direction (Ghost, Navigation.shortestPath).
5. Unit occupies / leaves a Square (Unit.occupy, leaveSquare).
