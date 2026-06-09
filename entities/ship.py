import math

import pygame

from entities.entity import Entity
from scripts.components.physics_component import PhysicsComponent
from scripts.components.ship_control_component import ShipControlComponent


class Ship(Entity):
    def __init__(self, x, y, width, height, handler):
        super().__init__(x, y, width, height, 0, 0, handler)

        self.add_component(ShipControlComponent())
        # Drag near 1.0 means momentum bleeds off slowly: the ship keeps drifting
        # at roughly the same speed/heading until thrust or a wall changes it.
        self.add_component(PhysicsComponent(drag=0.985))

    def update(self):
        self.get_component(ShipControlComponent).update()
        self.get_component(PhysicsComponent).update()
        self._clamp_to_map()

    def _clamp_to_map(self):
        physics = self.get_component(PhysicsComponent)
        bounds = self.handler.world.map_rect()

        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
            physics.velocity.x = 0
        elif self.rect.right > bounds.right:
            self.rect.right = bounds.right
            physics.velocity.x = 0

        if self.rect.top < bounds.top:
            self.rect.top = bounds.top
            physics.velocity.y = 0
        elif self.rect.bottom > bounds.bottom:
            self.rect.bottom = bounds.bottom
            physics.velocity.y = 0

    def render(self, surface, ref_pos):
        physics = self.get_component(PhysicsComponent)
        cx = self.rect.centerx - ref_pos[0]
        cy = self.rect.centery - ref_pos[1]
        half_w = self.rect.width / 2
        half_h = self.rect.height / 2

        # Local ship points: nose at +x, wings at -x (angle 0 = east)
        local = [
            (half_w, 0),
            (-half_w, -half_h),
            (-half_w, half_h),
        ]
        rad = math.radians(physics.angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        points = [
            (cx + x * cos_a - y * sin_a, cy + x * sin_a + y * cos_a)
            for x, y in local
        ]
        pygame.draw.polygon(surface, (220, 220, 240), points)
        pygame.draw.polygon(surface, (80, 80, 100), points, 2)
