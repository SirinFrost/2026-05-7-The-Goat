import pygame
from scripts.components.component import Component

class ControlComponent(Component):
    
    def __init__(self, entity, speed):
        super().__init__()
        self.speed = speed
        self.entity = entity
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.entity.x -= self.speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.entity.x += self.speed
        else:
            self.entity.vx = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.entity.y -= self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.entity.y += self.speed
        else:
            self.entity.vy = 0