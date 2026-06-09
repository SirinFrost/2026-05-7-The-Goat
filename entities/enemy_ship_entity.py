import math

import pygame

from entities.entity import Entity
from entities.projectile_entity import ProjectileEntity
from scripts.components.box_collider import BoxCollider
from scripts.components.health_component import HealthComponent
from scripts.components.physics_component import PhysicsComponent

ENEMY_SIZE = 32
ENEMY_THRUST_FORCE = 480.0  # seek acceleration toward the player, px/s^2 (20% slower)
ENEMY_TURN_SPEED = 140.0  # degrees/sec it can rotate its heading toward the player
ENEMY_SHOOT_RANGE = 300  # px; only fire when the player is closer than this
ENEMY_SHOOT_INTERVAL = 2.0  # seconds between an enemy's shots
ENEMY_FILL = (200, 70, 70)
ENEMY_OUTLINE = (90, 20, 20)


class EnemyShipEntity(Entity):
    """An enemy ship: motion + hitbox + health, drawn as a triangle that points along
    its heading. It drives its own behavior in update() (turn toward the player, thrust
    forward, shoot when in range). EnemySystem only decides when new enemies appear."""

    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_SIZE, ENEMY_SIZE, 0, 0, None)

        # The base Entity only tracks `rect`; this engine's colliders/handlers also
        # read x/y/width/height, so we keep them in sync with the rect.
        self.x = x
        self.y = y
        self.width = ENEMY_SIZE
        self.height = ENEMY_SIZE

        self.shoot_cooldown = 0.0  # seconds until it can fire again
        self.dead = False

        self.add_component(PhysicsComponent(drag=0.95))
        # category 0b0010 = enemy; mask 0b0101 = player ship (0b0001) + player projectiles (0b0100)
        self.add_component(
            BoxCollider(self, 0b0010, 0b0101, pygame.Rect(0, 0, ENEMY_SIZE, ENEMY_SIZE))
        )
        self.add_component(HealthComponent(hp=3))

    def update(self):
        # Seek the player like a real ship: turn the heading toward them over time, then
        # thrust forward along whatever direction we're now facing. This runs BEFORE
        # super().update() so PhysicsComponent integrates the new thrust this frame —
        # same control-then-physics order as the player's Ship.
        physics = self.get_component(PhysicsComponent)
        player = getattr(self.handler.world, "player", None)
        if player is not None:
            dt = self.handler.world.delta_time
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery

            # Rotate gradually toward the player. `diff` is the shortest signed angle to
            # the target (wrapped into -180..180); clamping it to the per-frame turn
            # budget is what makes the ship arc instead of snapping to face the player.
            desired = math.degrees(math.atan2(dy, dx))
            diff = (desired - physics.angle + 180) % 360 - 180
            max_turn = ENEMY_TURN_SPEED * dt
            physics.angle += max(-max_turn, min(max_turn, diff))

            # Thrust along the heading we're now facing (not straight at the player), so
            # the ship has to point itself the right way to close in.
            rad = math.radians(physics.angle)
            thrust = pygame.Vector2(math.cos(rad), math.sin(rad)) * ENEMY_THRUST_FORCE
            physics.velocity += thrust * dt

            # Shoot along the current heading when the player is in range and we're ready.
            distance = math.sqrt(dx ** 2 + dy ** 2)
            self.shoot_cooldown -= dt
            if distance < ENEMY_SHOOT_RANGE and self.shoot_cooldown <= 0:
                x, y = self.rect.center
                projectile = ProjectileEntity(x, y, angle=physics.angle)
                self.handler.add_entity(projectile)
                self.shoot_cooldown = ENEMY_SHOOT_INTERVAL

        super().update()  # PhysicsComponent integrates drag + movement
        self.x = self.rect.x
        self.y = self.rect.y

    def render(self, surface, ref_pos):
        # Draw a triangle pointing along the heading, same technique as the player Ship:
        # define the shape in local space (nose at +x), rotate by the heading angle, then
        # translate to the on-screen center. Visual heading == movement heading by design.
        physics = self.get_component(PhysicsComponent)
        cx = self.rect.centerx - ref_pos[0]
        cy = self.rect.centery - ref_pos[1]
        half_w = self.rect.width / 2
        half_h = self.rect.height / 2

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
        pygame.draw.polygon(surface, ENEMY_FILL, points)
        pygame.draw.polygon(surface, ENEMY_OUTLINE, points, 2)

    def delete(self):
        # Flag for removal; EntityHandler's dead-sweep does the actual kill so we
        # never mutate the entity dict mid-update.
        self.dead = True
