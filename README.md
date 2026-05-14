# The Goat

Practice project built with **[pygame-ce](https://pygame-ce.readthedocs.io/en/stable/)**: a simple 2D window with randomly spawned moving squares, wall bouncing, and a small entity/handler scaffold. Intended for portfolio work and experimentation.

## What it does

- Opens a **1280×720** resizable window titled *The Goat*
- Currently spawns **100 squares** at random positions, sizes, velocities, and colors inside the play area
- Runs the game loop at about **60 FPS** (delta time driven) and **prints smoothed FPS** to the console about once per second

## Requirements

- **Python** 3.14+ (see `pyproject.toml`)
- **[pygame-ce](https://github.com/pygame-community/pygame-ce)** 2.5.7+

## Setup

Install **pygame-ce** (matching `pyproject.toml`):

```bash
pip install "pygame-ce>=2.5.7"
```

If you use **[uv](https://github.com/astral-sh/uv)**:

```bash
uv sync
```

## Run

From the project root:

```bash
python main.py
```

## Project layout

| Path | Role |
|------|------|
| `main.py` | Window, game loop, entity setup |
| `entities/` | `Entity`, `Square`, `HunnedSquares` |
| `handlers/` | `EntityHandler` — update/render all entities |

## Development

Optional dev tools (formatter) are listed under `[dependency-groups]` dev in `pyproject.toml`.
