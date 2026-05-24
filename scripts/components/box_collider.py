from scripts.components.collider_component import ColliderComponent
import pygame

class BoxCollider(ColliderComponent):
    def __init__(self, entity, category_bits, mask_bits, shape):
        super().__init__(entity, category_bits, mask_bits, shape)
    
    def update(self):
        pass
        
    def render(self, window, ref_pos):
        e = self.entity
        draw_rect = pygame.Rect(e.x, e.y, e.width, e.height)
        pygame.draw.rect(window, (255, 0, 0), draw_rect, 2)