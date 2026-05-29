# Engine architecture map

Structural map of The Goat (a pygame-ce 2D teaching engine). This is a snapshot
that can drift — read the code before relying on it. See also
[project facts](project-facts.md).

- **Game loop** — `World.run()` in [handlers/world.py](../../handlers/world.py)
  drives everything: pump events → `update()` → `render()` → `tick()`. `tick()`
  computes delta time off a 60 FPS clock and prints smoothed FPS once a second.
- **Rendering** — draws to a fixed-size `frame_buffer`, then scales it to the
  window with letterboxing (`World.render()`). The standard "render at a virtual
  resolution, scale to fit" technique.
- **Entities** — [entities/entity.py](../../entities/entity.py) holds a `dict` of
  components and fans `update()`/`render()` out to each. `Square` and
  `HunnedSquares` build on it.
- **Components** — [scripts/components/](../../scripts/components/) has a
  `Component` base plus sprite, control, and collider (box/circle) components.
- **Handlers** — [handlers/](../../handlers/): `EntityHandler` (owns the entity
  collection), `PhysicsHandler` (wall collisions), `AssetManager` (image loading),
  `WindowHandler` (window + frame buffer).
- **World tiles** — [scripts/world/](../../scripts/world/) has `Tile` and `Chunk`
  for tilemap rendering; chunks live in `World.chunks` keyed by `"col_row"`.

**Note on "ECS":** the project is framed as ECS but is really the Unity-style
GameObject/Component model — components carry their own `update()`/`render()` and
the `Entity` stores state directly (`rect`, `velocity`, `vx`, `vy`). No standalone
systems yet; `World` hand-runs the physics pass. (This distinction is a deliberate
teaching point kept in the repo CLAUDE.md.)
