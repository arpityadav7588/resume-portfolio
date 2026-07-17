# Agent Workflow Rules

The following rules dictate the expected workflow for AI agents operating in this workspace:

1. **Brainstorming**: Whenever requested to brainstorm or design a solution, always output a formal design doc (e.g., `design_doc.md`).
2. **Writing Plans**: When creating implementation plans or task checklists, break the work down into very small, granular implementation tasks that take approximately 2-5 minutes each to complete.
3. **Using Git Worktrees**: When working on isolated features, experiments, or branches, utilize `git worktree` to create isolated branches rather than modifying the main working tree directly.
4. **Test-Driven Development**: When writing new code, follow strict TDD principles: RED (write a failing test first), GREEN (write minimal code to pass the test), REFACTOR (clean up the code).
5. **Minimal Change Engineering (Ponytail Mode)**: Maintain strict discipline against over-engineering. Embrace "standard lazy mode" (minimal viable diffs) by default. Review all diffs to prevent scope creep or premature abstractions, and apply ruthless simplicity to overly complex code.
6. **Subagent-Driven Development**: When executing implementation plans, delegate the execution of specific plan documents to specialized subagents or cheaper execution models to handle the implementation while maintaining the high-level strategy.
7. **Frontend Layout Optimization**: Utilize headless text measurement (e.g., `@chenglou/pretext`) to calculate text dimensions prior to DOM reflow. Use this specifically for virtualization, masonry layouts, and preventing Cumulative Layout Shift (CLS).
