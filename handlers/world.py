import pygame


from handlers.entity_handler import EntityHandler
from handlers.asset_manager import AssetManager
from handlers.physics_handler import PhysicsHandler
from handlers.window_handler import WindowHandler
from handlers.particle_handler import ParticleHandler
from handlers.triangle_particle_handler import TriangleParticleHandler

from handlers.scene_manager import SceneManager
from scripts.scenes.menu_scene import MenuScene
from scripts.scenes.play_scene import PlayScene







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
        self.scene_manager = SceneManager(self)
        self.scene_manager.add_scene(MenuScene())
        self.scene_manager.add_scene(PlayScene())

    def update(self):
        self.scene_manager.update()

    def render(self):
        frame_buffer = self.window_handler.frame_buffer
        window = self.window_handler.window
        window_size = window.get_size()
        frame_w, frame_h = self.window_handler.frame_size

        self.scene_manager.render(frame_buffer)

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
            else:
                self.scene_manager.handle_event(event)

        self.tick()
        self.update()
        self.render()
        return True
