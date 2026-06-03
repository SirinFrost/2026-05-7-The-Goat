import pygame

from scripts.scenes.scene import Scene


class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")

    def enter(self):
        # One-time setup when menu becomes active (fonts are expensive to recreate every frame)
        self._title_font = pygame.font.SysFont(None, 48)
        self._hint_font = pygame.font.SysFont(None, 28)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.manager.set_scene("play")

    def update(self):
        # Menu has no simulation — leave empty
        pass

    def render(self, frame_buffer):
        frame_buffer.fill((20, 30, 50))

        title = self._title_font.render("The Goat", True, (240, 240, 240))
        hint = self._hint_font.render(
            "Press Enter or Space to play", True, (180, 180, 180)
        )

        w, h = frame_buffer.get_size()
        frame_buffer.blit(title, title.get_rect(center=(w // 2, h // 2 - 30)))
        frame_buffer.blit(hint, hint.get_rect(center=(w // 2, h // 2 + 30)))