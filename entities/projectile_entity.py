import math

import pygame

from entities.entity import Entity
from scripts.components.box_collider import BoxCollider
from scripts.components.physics_component import PhysicsComponent


class ProjectileEntity(Entity):
    """A bullet: spawned at a position with a heading angle and speed. A
    PhysicsComponent owns the velocity and moves the rect; the bullet stays alive
    until it has travelled `max_distance`, then flags itself for removal. Distance
    (not screen edge) is the right cutoff once a camera makes off-screen still in play."""

    def __init__(self, x, y, angle, speed=600, max_distance=800):
        super().__init__(x, y, 4, 4, 0, 0, None)

        # The base Entity only tracks `rect`; this engine's colliders/handlers also
        # read x/y/width/height, so we keep them in sync with the rect.
        self.x = x
        self.y = y
        self.width = 4
        self.height = 4

        # PhysicsComponent owns motion. drag=1.0 means no slowdown — a bullet keeps
        # its speed for its whole flight. Velocity (px/s) is set once from the angle.
        physics = PhysicsComponent(drag=1.0)
        physics.angle = angle
        rad = math.radians(angle)
        physics.velocity = pygame.Vector2(math.cos(rad), math.sin(rad)) * speed
        self.add_component(physics)

        # category 0b0100 = projectile, mask 0b0010 = collides with enemies
        self.add_component(BoxCollider(self, 0b0100, 0b0010, pygame.Rect(0, 0, 4, 4)))

        self.max_distance = max_distance
        self.distance_traveled = 0.0
        self.dead = False

    def update(self):
        super().update()  # PhysicsComponent moves the rect by velocity * dt

        # Keep x/y aligned with the rect the physics component just moved.
        self.x = self.rect.x
        self.y = self.rect.y

        physics = self.get_component(PhysicsComponent)
        dt = self.handler.world.delta_time
        self.distance_traveled += physics.velocity.length() * dt
        if self.distance_traveled >= self.max_distance:
            self.delete()
            return

        # Die at the map edge — the same green boundary the ship can't cross. Once the
        # bullet's rect is no longer fully inside the map, it has touched the border.
        if not self.handler.world.map_rect().contains(self.rect):
            self.delete()

    def delete(self):
        # Flag for removal; EntityHandler's dead-sweep does the actual kill so we
        # never mutate the entity dict mid-update.
        self.dead = True

    def render(self, surface, ref_pos):
        screen_pos = (
            int(self.rect.centerx - ref_pos[0]),
            int(self.rect.centery - ref_pos[1]),
        )
        pygame.draw.circle(surface, (255, 255, 255), screen_pos, 2)
