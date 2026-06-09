import pygame

from scripts.components.component import Component


class PhysicsComponent(Component):
    def __init__(self, drag=0.98, max_speed=None):
        super().__init__()
        self.velocity = pygame.Vector2(0, 0)  # pixels per second
        self.angle = 0.0  # heading in degrees
        self.drag = drag  # fraction of speed retained each 1/60 s
        self.max_speed = max_speed  # optional hard cap on speed (px/s); None = uncapped

    def update(self):
        dt = self.entity.handler.world.delta_time

        # Frame-rate independent: drag is the retention per 1/60 s, generalized to
        # any dt, and position advances by velocity (px/s) * dt.
        self.velocity *= self.drag ** (dt * 60)

        # Optional speed cap. Whoever owns the cap (e.g. the ship's control component)
        # sets max_speed; we just enforce it so it holds during drift too, not only
        # while thrusting.
        if self.max_speed is not None and self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.entity.rect.x += self.velocity.x * dt
        self.entity.rect.y += self.velocity.y * dt
