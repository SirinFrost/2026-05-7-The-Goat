import random

from entities.enemy_ship_entity import EnemyShipEntity


class EnemySystem:
    """Spawns enemy ships around the edge of the camera view. That's all it does now —
    each enemy seeks and shoots on its own in EnemyShipEntity.update(). The system owns
    the one decision that isn't per-entity: when a new enemy should appear."""

    def __init__(self, world, spawn_interval=3.0, max_enemies=6):
        self.world = world
        self.spawn_timer = 0.0
        self.spawn_interval = spawn_interval  # seconds between spawns
        self.max_enemies = max_enemies  # population cap; don't spawn past this

    def update(self):
        dt = self.world.delta_time

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            # Only spawn while under the cap; otherwise reset the timer and try again
            # next interval, so a new enemy appears soon after one dies.
            if self._enemy_count() < self.max_enemies:
                self._spawn_enemy()
            self.spawn_timer = 0.0

    def _enemy_count(self):
        return sum(
            1
            for entity in self.world.entity_handler.entities.values()
            if isinstance(entity, EnemyShipEntity)
        )

    def _spawn_enemy(self):
        # Spawn just outside the camera view around the player, so enemies stream in
        # from the screen edges instead of from a fixed corner of the large map.
        frame_w, frame_h = self.world.window_handler.frame_size
        px, py = self.world.player.rect.center
        margin = 48

        left = px - frame_w // 2 - margin
        right = px + frame_w // 2 + margin
        top = py - frame_h // 2 - margin
        bottom = py + frame_h // 2 + margin

        edge = random.choice(("top", "bottom", "left", "right"))
        if edge == "top":
            x, y = random.randint(left, right), top
        elif edge == "bottom":
            x, y = random.randint(left, right), bottom
        elif edge == "left":
            x, y = left, random.randint(top, bottom)
        else:  # right
            x, y = right, random.randint(top, bottom)

        # Keep spawns inside the playable map (with a margin) so enemies don't appear in
        # the void and so the bullets they fire don't start already past the border.
        bounds = self.world.map_rect()
        x = max(bounds.left + 32, min(bounds.right - 32, x))
        y = max(bounds.top + 32, min(bounds.bottom - 32, y))

        enemy = EnemyShipEntity(x, y)
        self.world.entity_handler.add_entity(enemy)
