from entities.entity import Entity
import pygame
import uuid

class Square(Entity):
    def __init__(self, x, y, width, height, vx , vy):
        super().__init__(x, y, width, height, vx, vy)
        self.id = uuid.uuid4()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.draw.rect(self.image, (123, 0, 123, 128), self.image.get_rect())
        self.color = (124, 69, 67)
        self.speed = 5
        self.direction = pygame.Vector2(0, 0)

        

    def update(self):
        super().update()
        # Keyboard controlled movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        # Wall collision based bouncing.
        # if self.x < 0:
        #     self.vx = -self.vx
        # if self.x + self.width > 1280:
        #     self.vx = -self.vx
        # if self.y < 0:
        #     self.vy = -self.vy
        # if self.y + self.height > 720:
        #     self.vy = -self.vy

        # Wall collision based sliding
        if self.x < 0:
            self.x = 0
            self.vx = 0
        if self.x + self.width > 1280:
            self.x = 1280 - self.width
            self.vx = 0
        if self.y < 0:
            self.y = 0
            self.vy = 0
        if self.y + self.height > 720:
            self.y = 720 - self.height
            self.vy = 0

        self.x += self.vx
        self.y += self.vy

        self.rect.x = self.x
        self.rect.y = self.y


    
    def render(self, surface, ref_pos):
        super().render(surface, ref_pos)
        surface.blit(self.image, self.rect)
