import pygame
import uuid
from components.component import Component


class Entity:
    def __init__(self, x, y, width, height, vx, vy):
        self.id = uuid.uuid4()
        self.rect = pygame.Rect(x, y, width, height)   # position + size in one place
        self.components: dict[type[Component], Component] = {}
        self.handler = None
        self.velocity = pygame.Vector2(0, 0)
        self.vx = vx
        self.vy = vy

    def update(self):
        for component in self.components.values():
            component.update()
    def render(self, surface, ref_pos):
        for component in self.components.values():
            component.render(surface, ref_pos)
    def delete(self):
        pass