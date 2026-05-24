import pygame
from components.component import Component

class SpriteComponent(Component):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

    def render(self, window, pos):
        window.blit(self.surface, pos)