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
from scripts.scenes.shop_scene import ShopScene
from scripts.upgrades import Upgrades







class World:
    def __init__(self):
        self.chunks = {}
        self.clock = pygame.time.Clock()
        self.delta_time = 0.0
        self.timer = 0.0
        self.player = None  # set by the active scene; entities seek it
        # Two rectangles, both centered on the same point:
        #   map_size   = the green play area (the "map" the background fill covers)
        #   world_size = the outer border/wall the ship is clamped to. It's larger than
        #                the map, so the ship can sail off the green into a void before
        #                hitting the wall.
        self.map_size = (7168, 4032)
        self.world_size = (9728, 6592)

        # Player-wide progression, kept on the world so it survives scene switches
        # (the shop spends money to raise upgrade levels; the ship reads the values).
        self.money = 0
        self.upgrades = Upgrades()

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
        self.scene_manager.add_scene(ShopScene())

    def map_rect(self):
        """The green play area as a rect in world coordinates, centered inside the
        larger world border. Single source of truth for the playable boundary: the
        ship clamps to it, bullets die at it, and the background is painted over it."""
        map_w, map_h = self.map_size
        world_w, world_h = self.world_size
        return pygame.Rect(
            (world_w - map_w) // 2,
            (world_h - map_h) // 2,
            map_w,
            map_h,
        )

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
