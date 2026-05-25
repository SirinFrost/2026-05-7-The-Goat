from entities.entity import Entity
import pygame
import uuid
from scripts.components.control_component import ControlComponent
from scripts.components.box_collider import BoxCollider

class Square(Entity):
    def __init__(self, x, y, width, height, vx , vy, handler):
        super().__init__(x, y, width, height, vx, vy, handler)
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
        box_collider = BoxCollider(self, 1, 1, pygame.Rect(x, y, width, height))
        self.add_component(box_collider)
        

    def update(self):
        super().update()
        # Keyboard controlled movement
        control_component = ControlComponent(self, self.speed)
        self.components[ControlComponent] = control_component

        # Wall collision based bouncing.
        # if self.x < 0:
        #     self.vx = -self.vx
        # if self.x + self.width > 1280:
        #     self.vx = -self.vx
        # if self.y < 0:
        #     self.vy = -self.vy
        # if self.y + self.height > 720:
        #     self.vy = -self.vy

        frame_width, frame_height = self.handler.world.window_handler.frame_size

        # Wall collision based sliding
        if self.x < 0:
            self.x = 0
            self.vx = 0
        if self.x + self.width > frame_width:
            self.x = frame_width - self.width
            self.vx = 0
        if self.y < 0:
            self.y = 0
            self.vy = 0
        if self.y + self.height > frame_height:
            self.y = frame_height - self.height
            self.vy = 0

        self.x += self.vx
        self.y += self.vy

        self.rect.x = self.x
        self.rect.y = self.y


    
    def render(self, surface, ref_pos):
        for component in self.components.values():
            component.render(surface, ref_pos)
        surface.blit(self.image, self.rect)
        
