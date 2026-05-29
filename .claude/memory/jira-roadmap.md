# JIRA roadmap

Two epics drive this project. **We are currently focused on the engine epic.**
See also [project facts](project-facts.md) for the JIRA link.

- **GAME-2 — Build a Simple ECS Game Engine** (current focus). Sections 0–8.
- **GAME-136 — Build a Ship Survival Game** (later). Sections 9–10: ship,
  projectiles, enemies, waves, camera, health, HUD, scoring.

Tickets are organized into numbered sections; each section has tasks (`[N.x]`)
and some have subtasks (`[N.xa]`). This is a snapshot — JIRA status and git are
the live sources of truth.

## Engine epic (GAME-2) sections

- **[0]** Git + environment setup (uv, pygame-ce, black). — GAME-32
- **[1]** Pygame window, drawing shapes, keyboard polling. — GAME-3/4/5
- **[2]** Project structure, `Entity` base class, `EntityHandler`, first `Square`. — GAME-6/7/8 (+subtasks)
- **[3]** Velocity via `Vector2`, bouncing, 100-entity stress test, FPS readout. — GAME-9/10/11
- **[4]** Component pattern: `Component` base, `ControlComponent`, `Entity` holds a component dict. — GAME-12/13
- **[5]** Collision/physics: `ColliderComponent` + bitmask filtering, `Box`/`CircleCollider`, `PhysicsHandler`. — GAME-15/16/17
- **[6]** Assets/world: `AssetManager` (cached image load), `SpriteComponent`, `World` owning the managers, two-pass update/render loop. — GAME-18/19/20
- **[7]** Tiles/chunks: `Tile`, `Chunk` (16×16), `ChunkRenderer` (bake tiles to one surface), `LevelLoader` (JSON levels). — GAME-21/22/23
- **[8]** Particles + delta time: injectable-function `ParticleHandler`, triangle/sprite particle effects, on-death swap. — GAME-24/25/26/27

## Progress (as of 2026-05-28)

Merged into `main` (via PRs #1–#11), mapped to sections:

- **Sections 0–6: complete and merged.** Parent tasks marked Done in JIRA.
- **Section 7 (tiles/chunks): part 1 merged** (PR #11, chunk/tile classes).
  GAME-21/22/23 sit at **In Review** in JIRA.
- **Section 8 (particles): not merged.** GAME-24 In Progress, rest To Do.
- Sections 9–10 (the game epic, GAME-136): not started.

### Status hygiene note

Several section 5/6/7 **subtasks** are still `To Do` in JIRA even though their
parent task is `Done` and the code is merged (e.g. GAME-39/40/41 under physics,
GAME-62/64 under assets). The parent-task status and the repo are ahead of the
subtask checkboxes. Trust git + the parent status over subtask status. GAME-63
is cancelled (folded into the `World`-owns-`AssetManager` approach).
