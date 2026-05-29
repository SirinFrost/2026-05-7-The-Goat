# Memory index

Manifest of the durable project context for The Goat. The notes themselves live in
[memory/](memory/). Read the file whose hook matches your task; read all of them
when starting fresh. These notes are snapshots and can drift — the code at HEAD and
live JIRA/git are the sources of truth when they disagree.

- [memory/engine-architecture.md](memory/engine-architecture.md) — structural map of
  the codebase: game loop, render/update split, entities, components, handlers,
  world tiles, and the "ECS is really a Component pattern" note.
- [memory/project-facts.md](memory/project-facts.md) — fixed facts: JIRA project
  link, the two epics, Python and pygame-ce versions.
- [memory/jira-roadmap.md](memory/jira-roadmap.md) — the JIRA roadmap: both epics,
  the numbered engine sections (0–8), and current progress / status-hygiene notes.

When you add, remove, or rename a file in [memory/](memory/), update this index in
the same change so it stays a complete manifest of what's in that directory.
