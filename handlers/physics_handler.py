import pygame
from scripts.components.collider_component import ColliderComponent

class PhysicsHandler:
    def __init__(self, entity_handler):
        self.entity_handler = entity_handler

    def update(self):
        entities = list(self.entity_handler.entities.values())
        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                entity_a = entities[i]
                entity_b = entities[j]

                colliders_a = [
                    c for c in entity_a.components.values()
                    if isinstance(c, ColliderComponent)]

                colliders_b = [
                    c for c in entity_b.components.values()
                    if isinstance(c, ColliderComponent)]

                if not colliders_a or not colliders_b:
                    continue
                
                for collider_a in colliders_a:
                    for collider_b in colliders_b:
                        if (collider_a.category_bits & collider_b.mask_bits) == 0:
                            continue
                        if (collider_a.mask_bits & collider_b.category_bits) == 0:
                            continue
                        
                        rect_a = collider_a.shape.copy()
                        rect_a.topleft = collider_a.entity.rect.topleft
                        
                        rect_b = collider_b.shape.copy()
                        rect_b.topleft = collider_b.entity.rect.topleft

                        if not rect_a.colliderect(rect_b):
                            continue
                        
                        self.handle_collision(collider_a, collider_b)



    def handle_collision(self, collider_a, collider_b):
        pass
    
    def handle_wall_collision(self, entity):
        if entity.x < 0:
            entity.vx = -entity.vx
        if entity.x + entity.width > 1280:
            entity.vx = -entity.vx
        if entity.y < 0:
            entity.vy = -entity.vy
        if entity.y + entity.height > 720:
            entity.vy = -entity.vy