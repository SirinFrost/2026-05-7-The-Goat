import pygame

from scripts.components.component import Component


class SpriteComponent(Component):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

    def render(self, window, ref_pos):
        pos = (self.entity.rect.x - ref_pos[0], self.entity.rect.y - ref_pos[1])
        window.blit(self.surface, pos)
