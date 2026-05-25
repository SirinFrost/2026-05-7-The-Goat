import pygame

class Tile:
    def __init__(self, chunk_x, chunk_y, image, TILE_SIZE):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.image = image
        self.TILE_SIZE = TILE_SIZE
    
    def update(self):
        pass
    
    def render(self, window, ref_pos):
        window.blit(self.image, (self.chunk_x * self.TILE_SIZE - ref_pos[0], self.chunk_y * self.TILE_SIZE - ref_pos[1]))