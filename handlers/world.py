import pygame
import random
import math

from handlers.entity_handler import EntityHandler
from handlers.asset_manager import AssetManager
from handlers.physics_handler import PhysicsHandler
from handlers.window_handler import WindowHandler
from handlers.particle_handler import ParticleHandler
from handlers.triangle_particle_handler import TriangleParticleHandler


class World:
    def __init__(self):
        self.chunks = {}
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0
        self.timer = 0.0

        self.asset_manager = AssetManager(self)
        self.window_handler = WindowHandler(
            self, (720, 360), (1280, 720), pygame.RESIZABLE, "The Goat", True)
        self.entity_handler = EntityHandler(self)
        self.particle_handler = ParticleHandler(self)
        self.physics_handler = PhysicsHandler(self)
        self.triangle_particle_handler = TriangleParticleHandler(self)
        
    def update(self):
        self.entity_handler.update()
        for entity in self.entity_handler.entities.values():
            self.physics_handler.handle_wall_collision(entity)
        self.physics_handler.update()
        self.particle_handler.update()
        self.triangle_particle_handler.update()

    def render(self):
        frame_buffer = self.window_handler.frame_buffer
        frame_buffer.fill((2, 69, 0))

        for chunk in self.chunks.values():
            chunk.render(frame_buffer, (0, 0))

        self.entity_handler.render(frame_buffer, (0, 0))
        self.particle_handler.render(frame_buffer, (0, 0))
        self.triangle_particle_handler.render(frame_buffer, (0, 0))

        window = self.window_handler.window
        window_size = window.get_size()
        frame_w, frame_h = self.window_handler.frame_size
        scale = min(window_size[0] / frame_w, window_size[1] / frame_h)
        scaled_size = (int(frame_w * scale), int(frame_h * scale))
        scaled = pygame.transform.scale(frame_buffer, scaled_size)

        window.fill(self.window_handler.letterbox_color)
        offset = (
            (window_size[0] - scaled_size[0]) // 2,
            (window_size[1] - scaled_size[1]) // 2,
        )
        window.blit(scaled, offset)
        pygame.display.flip()

    def tick(self):
        self.delta_time = self.clock.tick(60) / 1000.0
        self.timer += self.delta_time
        if self.timer >= 1.0:
            print(self.clock.get_fps())
            self.timer = 0.0

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.window_handler.resize(event.size)

        for i in range(10):
            x_velocity = random.randint(-100, 100)
            y_velocity = random.randint(-100, 100)
            self.particle_handler.add_particle(0, 0, 2, (255, 0, 0), x_velocity, y_velocity, 1.0)
        
        for i in range(10):
            x_velocity = random.randint(-100, 100)
            y_velocity = random.randint(-100, 100)
            self.triangle_particle_handler.add_particle(
                360, 180, 2, (0, 255, 0),
                random.randint(-100, 100), random.randint(-100, 100), 1.0,
                angle=random.uniform(0, math.tau),           # starting orientation
                angular_velocity=random.uniform(-4, 4),      # ~ full turn every 1–2 sec
                )

        self.tick()
        self.update()
        self.render()
        return True
