import pygame


class WindowHandler:
    def __init__(self, world, frame_size, window_size, flags, title, vsync):
        self.world = world
        self.frame_size = frame_size
        self.flags = flags
        self.vsync = vsync
        self.letterbox_color = (0, 0, 0)
        self.window = pygame.display.set_mode(window_size, flags, vsync)
        pygame.display.set_caption(title)
        self.frame_buffer = pygame.Surface(frame_size).convert_alpha()

    def resize(self, size):
        self.window = pygame.display.set_mode(size, self.flags, self.vsync)
