import pygame


class WindowHandler:
    def __init__(self, frame_size, window_size, flags, title, vsync):
        self.frame_size = frame_size
        self.flags = flags
        self.vsync = vsync
        self.letterbox_color = (0, 0, 0)
        self.window = pygame.display.set_mode(window_size, flags, vsync)
        pygame.display.set_caption(title)
        self.frame_buffer = pygame.Surface(frame_size).convert_alpha()

    def resize(self, size):
        self.window = pygame.display.set_mode(size, self.flags, self.vsync)

    def present(self):
        window_size = self.window.get_size()
        frame_w, frame_h = self.frame_size
        scale = min(window_size[0] / frame_w, window_size[1] / frame_h)
        scaled_size = (int(frame_w * scale), int(frame_h * scale))
        scaled = pygame.transform.scale(self.frame_buffer, scaled_size)

        self.window.fill(self.letterbox_color)
        offset = (
            (window_size[0] - scaled_size[0]) // 2,
            (window_size[1] - scaled_size[1]) // 2,
        )
        self.window.blit(scaled, offset)
