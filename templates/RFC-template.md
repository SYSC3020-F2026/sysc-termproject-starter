# RFC: Detailed design & design patterns — <subsystem name>

*Deliverable of Sprint 4. Commit to `docs/rfc/`. This documents the detailed design of your subsystem and the Lecture 9 patterns it uses.*

- **Authors:** <names>
- **Status:** Draft | Reviewed | Final
- **Reviewers:** <teammate(s)> — approved via PR #___

## 1. Summary
One paragraph: what this subsystem does and the design story you are documenting.

## 2. Design overview
A design class diagram of the subsystem (PlantUML in the repo, image linked here) and a short walkthrough.

## 3. Design patterns
For each pattern present, fill one block. Include **≥ 1 behavioural** and **≥ 1 creational or structural** pattern.

### Pattern: <e.g., Strategy>
- **Category:** Behavioural | Structural | Creational
- **Intent (Lecture 9):** <one line>
- **Where it appears / roles:** <which classes play Context, Strategy, etc.>
- **Why it fits here:** <reasoning>
- **Class diagram:** <link to PlantUML image>
- **Code evidence:** <class / file references>

*(Copy the block per pattern. Candidates in this game: State, Strategy, Builder, Observer.)*

## 4. Modular-design quality (Lecture 8)
- **Cohesion:** where is it high / low, and why?
- **Coupling:** where is it low / high, and why?
- **Static-analysis evidence:** SonarCloud metrics (cyclomatic complexity, coupling, cohesion) for the subsystem; note any high-severity findings and whether they became defects.

## 5. Design goals & trade-offs
Which quality attributes the design favours (e.g., readability of control logic vs. runtime performance) and the trade-offs involved.

## 6. Traceability
Update the RTM: link each documented design element back to its requirement(s) and forward to the class(es) that implement it.
