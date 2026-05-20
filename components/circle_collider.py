from components.collider_component import ColliderComponent
import pygame

class CircleCollider(ColliderComponent):
    def __init__(self, entity, category_bits, mask_bits, shape):
        super().__init__(entity, category_bits, mask_bits, shape)
    
    def update(self):
        pass
        
    def render(self, window, ref_pos):
        e = self.entity
        draw_circle = pygame.draw.circle(window, (255, 0, 0), e.x, e.y, e.radius)
        pygame.draw.circle(window, (255, 0, 0), draw_circle, 2)