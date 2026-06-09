import math

import pygame

from entities.projectile_entity import ProjectileEntity
from scripts.components.component import Component
from scripts.components.physics_component import PhysicsComponent


class ShipControlComponent(Component):
    """Reads input and influences PhysicsComponent — turn heading, add thrust to
    velocity, and fire projectiles on a cooldown."""

    SPREAD_PER_BULLET = 8.0  # degrees between adjacent bullets when firing multiple

    def __init__(self, turn_speed=180.0):
        super().__init__()
        self.turn_speed = turn_speed  # degrees per second
        self.shoot_cooldown = 0  # seconds until the ship can fire again

    def update(self):
        physics = self.entity.get_component(PhysicsComponent)
        if physics is None:
            return

        dt = self.entity.handler.world.delta_time
        upgrades = self.entity.handler.world.upgrades
        keys = pygame.key.get_pressed()

        # The cap is a ship stat (data) enforced by PhysicsComponent (behavior). Push the
        # current upgraded value down each frame so buying it takes effect immediately.
        physics.max_speed = upgrades.max_speed.value

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            physics.angle -= self.turn_speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            physics.angle += self.turn_speed * dt

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rad = math.radians(physics.angle)
            thrust = (
                pygame.Vector2(math.cos(rad), math.sin(rad))
                * upgrades.acceleration.value
            )
            physics.velocity += thrust * dt

        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self._fire(physics.angle, upgrades)
            self.shoot_cooldown = 0.3  # seconds between shots
        self.shoot_cooldown -= dt

    def _fire(self, heading, upgrades):
        x, y = self.entity.rect.center
        count = int(upgrades.bullet_count.value)
        speed = upgrades.bullet_speed.value

        # Center the spread on the heading: e.g. 3 bullets -> offsets [-spread, 0, +spread].
        total_spread = self.SPREAD_PER_BULLET * (count - 1)
        start = heading - total_spread / 2
        for i in range(count):
            angle = start + self.SPREAD_PER_BULLET * i
            projectile = ProjectileEntity(x, y, angle, speed=speed)
            self.entity.handler.add_entity(projectile)
