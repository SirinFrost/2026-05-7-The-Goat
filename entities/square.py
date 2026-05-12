from entities.entity import Entity
import pygame
import uuid

class Square(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.draw.rect(self.image, (123, 0, 123, 128), self.image.get_rect())
        self.color = (124, 69, 67)
        self.speed = 5

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.x = self.x
        self.rect.y = self.y

    
    def render(self, surface, ref_pos):
        super().render(surface, ref_pos)
        surface.blit(self.image, self.rect)
