import pygame

from entities.ship import Ship
from handlers.enemy_system import EnemySystem
from scripts.components.collider_component import ColliderComponent
from scripts.scenes.scene import Scene
from scripts.world.level_loader import LevelLoader


class PlayScene(Scene):
    # Color stops for the concentric map gradient, from center outward to the border.
    MAP_CENTER_COLOR = (2, 69, 0)  # green  - center
    MAP_MIDDLE_COLOR = (130, 35, 35)  # red    - middle
    MAP_EDGE_COLOR = (30, 50, 120)  # blue   - rim, closest to the border
    # Where red sits between center (0.0) and edge (1.0). Pulling it inward squeezes the
    # green+red core into a smaller center and hands the larger outer band to blue.
    MAP_MIDDLE_STOP = 0.3
    # How many nested rects approximate the blend. More = smoother, but more draw calls.
    MAP_GRADIENT_STEPS = 120

    @staticmethod
    def _lerp_color(a, b, t):
        return (
            int(a[0] + (b[0] - a[0]) * t),
            int(a[1] + (b[1] - a[1]) * t),
            int(a[2] + (b[2] - a[2]) * t),
        )

    def _map_color(self, progress):
        """progress: 0.0 at the center, 1.0 at the map edge. The gradient runs through
        two segments — center->middle below MAP_MIDDLE_STOP, middle->edge above it."""
        stop = self.MAP_MIDDLE_STOP
        if progress < stop:
            return self._lerp_color(
                self.MAP_CENTER_COLOR, self.MAP_MIDDLE_COLOR, progress / stop
            )
        return self._lerp_color(
            self.MAP_MIDDLE_COLOR, self.MAP_EDGE_COLOR, (progress - stop) / (1 - stop)
        )

    def __init__(self):
        super().__init__("play")
        self.enemy_system = None
        # HUD font. Safe to build here: World (and so this scene) is created after
        # pygame.init(), which starts the font module.
        self._hud_font = pygame.font.SysFont(None, 20)

    def enter(self):
        """Becomes active on menu → play AND on shop → play. Only build the world on a
        real (re)start; returning from the shop must resume the same game, not wipe it.
        The live ship still in the world is our signal that a game is already running."""
        if self.world.player is not None:
            return

        world = self.world

        world.chunks.clear()
        world.entity_handler.entities.clear()
        world.particle_handler.particles.clear()
        world.triangle_particle_handler.particles.clear()

        LevelLoader(world, "assets/levels/level_01.json")

        # Start the ship in the middle of the (large) world so it has room to roam
        # in every direction; the camera will keep it centered on screen.
        world_w, world_h = world.world_size
        size = 32
        ship = Ship(
            world_w // 2 - size // 2,
            world_h // 2 - size // 2,
            size,
            size,
            world.entity_handler,
        )
        world.entity_handler.add_entity(ship)

        # Expose the player so seeking entities (enemies) can find it.
        world.player = ship

        # Recreated on each fresh run so the spawn timer starts clean. It only needs the
        # world now (it reaches the player via world.player when spawning).
        self.enemy_system = EnemySystem(world)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            self.manager.set_scene("menu")
        elif event.key == pygame.K_p:
            self.manager.set_scene("shop")

    def update(self):
        world = self.world

        # Run enemy AI before the entities integrate, so this frame's seek force is
        # applied before PhysicsComponent moves them.
        self.enemy_system.update()

        world.entity_handler.update()
        for entity in world.entity_handler.entities.values():
            if entity.get_component(ColliderComponent) is not None:
                world.physics_handler.handle_wall_collision(entity)
        world.physics_handler.update()
        world.particle_handler.update()
        world.triangle_particle_handler.update()

    def render(self, frame_buffer):
        world = self.world

        # Void everywhere first; the green map is then painted only over its own
        # rectangle, so the fill is "cut off" at the map edge and the space between the
        # map and the outer wall reads as empty void.
        frame_buffer.fill((0, 0, 0))

        # Camera: offset everything by the player's position so the player draws at
        # the center of the frame. ref_pos is the world coord at the top-left of view.
        ref_pos = self._camera_offset()

        # The map (same boundary the ship/bullets obey) is drawn as many concentric
        # rects whose color is interpolated by distance from the center. Painting
        # outer -> inner lets each smaller rect cover the previous one, so the stack of
        # thin rings reads as a smooth blend instead of hard color bands.
        map_rect = world.map_rect().move(-ref_pos[0], -ref_pos[1])
        steps = self.MAP_GRADIENT_STEPS
        for i in range(steps):
            scale = 1.0 - i / steps  # 1.0 at the edge -> ~0 at the center
            layer = map_rect.inflate(
                -int(map_rect.width * (1 - scale)),
                -int(map_rect.height * (1 - scale)),
            )
            pygame.draw.rect(frame_buffer, self._map_color(scale), layer)

        for chunk in world.chunks.values():
            chunk.render(frame_buffer, ref_pos)

        world.entity_handler.render(frame_buffer, ref_pos)
        world.particle_handler.render(frame_buffer, ref_pos)
        world.triangle_particle_handler.render(frame_buffer, ref_pos)

        self._draw_shop_hint(frame_buffer)

    def _draw_shop_hint(self, frame_buffer):
        # HUD is screen-space: drawn last, with no camera offset, so it stays pinned to
        # the corner regardless of where the ship is in the world.
        text = self._hud_font.render("Press P to open shop", True, (240, 240, 240))
        pad = 6
        # SRCALPHA gives the backing surface a per-pixel alpha channel; the 4th color
        # value (140/255) is what makes the panel see-through.
        panel = pygame.Surface(
            (text.get_width() + pad * 2, text.get_height() + pad * 2), pygame.SRCALPHA
        )
        panel.fill((0, 0, 0, 140))

        margin = 8
        x = frame_buffer.get_width() - panel.get_width() - margin
        frame_buffer.blit(panel, (x, margin))
        frame_buffer.blit(text, (x + pad, margin + pad))

    def _camera_offset(self):
        world = self.world
        frame_w, frame_h = world.window_handler.frame_size
        player = world.player
        if player is None:
            return (0, 0)
        return (
            player.rect.centerx - frame_w // 2,
            player.rect.centery - frame_h // 2,
        )
