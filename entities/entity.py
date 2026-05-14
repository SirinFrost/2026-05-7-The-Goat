import pygame
import uuid


class Entity:
    def __init__(self, x, y, width, height, vx, vy):
        self.id = uuid.uuid4()
        self.rect = pygame.Rect(x, y, width, height)   # position + size in one place
        self.components = {}
        self.handler = None
        self.velocity = pygame.Vector2(0, 0)
        self.vx = vx
        self.vy = vy

    def update(self):
        pass
    def render(self, surface, ref_pos):
        pass
    def delete(self):
        pass