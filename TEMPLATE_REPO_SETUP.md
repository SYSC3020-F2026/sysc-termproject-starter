% Building the GitHub Classroom Template Repo — exact steps
% SYSC term project (JPacman)

JPacman (`SERG-Delft/jpacman`) is a **self-contained Gradle project** — no companion libraries, and static analysis (Checkstyle/PMD/SpotBugs) plus JaCoCo coverage are built in. So the template is just *JPacman + your classroom files*.

# 0. Prerequisites
JDK (match the JPacman Gradle wrapper — 11 is safe), Git, a GitHub account. Check: `java -version`, `git --version`.

# 1. Build JPacman once locally

```bash
git clone https://github.com/SERG-Delft/jpacman
cd jpacman
chmod +x ./gradlew
./gradlew build            # compiles, runs tests, JaCoCo report, Checkstyle/PMD/SpotBugs
./gradlew run              # optional: play a round
cd ..
```
The JaCoCo CSV lands at `build/reports/jacoco/test/jacocoTestReport.csv`.

# 2. Create the GitHub organization
GitHub → **+** (top right) → **New organization** → Free plan → name it (e.g. `SYSC-4101`).

# 3. Build the template repository

```bash
cp -r jpacman sysc-termproject-starter
cp -r /path/to/TermProject/ClassroomStarter/. sysc-termproject-starter/
cd sysc-termproject-starter
./gradlew build            # must succeed and produce the JaCoCo report
git add -A && git commit -m "SYSC term-project starter (JPacman + autograding)"
```
Keep JPacman's `LICENSE` (CC-BY-SA / MIT as applicable) and add an attribution line to `README.md`.

Push to the org (create an **empty** repo in the org first — New repository, no README):

```bash
git remote add origin https://github.com/<org>/sysc-termproject-starter.git
git branch -M main && git push -u origin main
```

# 4. Mark it a template + set the coverage scope
- Repo -> **Settings** -> check **Template repository**.
- **Settings -> Secrets and variables -> Actions -> Variables -> New repository variable**: `COVERAGE_SCOPE = board,level,npc`.
- (No SonarCloud secret needed — static analysis is built into the Gradle build.)

# 5. Create the Classroom + roster
- <https://classroom.github.com> -> **New classroom** -> select your org -> name it.
- **Students** -> **Update roster** -> upload a CSV of student IDs.

# 6. Create the group assignment
- **New assignment -> Group assignment**; title; **Team size 3**; **Private**.
- **Starter code -> a template repository ->** `sysc-termproject-starter` -> **Create**.

# 7. Get the invite link
Assignment page -> **Copy invite link** (`https://classroom.github.com/a/...`) -> post on Brightspace.

---

**Why this is simpler than a Maven multi-repo game:** JPacman has no external companion libraries, so `./gradlew build` works out of the box — nothing to pre-install. The autograding workflows use `./gradlew` and the coverage checker reads the Gradle JaCoCo report.
