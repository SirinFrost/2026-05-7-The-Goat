from handlers.entity_handler import EntityHandler
from handlers.asset_manager import AssetManager
from handlers.physics_handler import PhysicsHandler
from handlers.window_handler import WindowHandler
import pygame


class World:
    def __init__(self):
        self.entity_handler = EntityHandler(AssetManager())
        self.physics_handler = PhysicsHandler(self.entity_handler)
        self.window_handler = WindowHandler((1280, 720), (1280, 720), pygame.RESIZABLE, "The Goat", True)
        self.asset_manager = AssetManager()
        self.chunks = {} # key is "x_y" "1_1" "1_2" "2_1" "2_2" etc.
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0
        self.timer = 0.0

    def update(self):
        self.entity_handler.update()
        for entity in self.entity_handler.entities.values():
            self.physics_handler.handle_wall_collision(entity)
        self.physics_handler.update()

    def render(self):
        self.window_handler.frame_buffer.fill((155, 69, 0))
        self.entity_handler.render(self.window_handler.frame_buffer, (0, 0))
        self.window_handler.present()
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

        self.update()
        # for chunk in self.chunks.values():
        #     chunk.update()
        self.render()
        # for chunk in self.chunks.values():
        #     chunk.render()
        self.tick()
        return True