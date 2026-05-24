from scripts.components.component import Component
import pygame

class ColliderComponent(Component):
    def __init__(self, entity, category_bits, mask_bits, shape):
        super().__init__()
        self.entity = entity
        self.category_bits = category_bits
        self.mask_bits = mask_bits  
        self.shape = shape

    