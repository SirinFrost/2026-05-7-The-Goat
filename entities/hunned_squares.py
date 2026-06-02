from entities.entity import Entity
import pygame
import uuid
import random

class HunnedSquares(Entity):
    def __init__(self, x, y, width, height, vx , vy, handler):
        super().__init__(x, y, width, height, vx, vy, handler)
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.draw.rect(self.image, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 128), self.image.get_rect())
        self.speed = 5
        self.direction = pygame.Vector2(0, 0)
        

    def update(self):
        super().update()
        dt = self.handler.world.delta_time
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.rect.x = self.x
        self.rect.y = self.y


    
    def render(self, surface, ref_pos):
        super().render(surface, ref_pos)
        surface.blit(self.image, self.rect)
