import pygame
from scripts.world.tile import Tile

class ChunkRenderer:
    def __init__(self, chunk):
        self.chunk = chunk
        chunk_pixel_size = chunk.CHUNK_SIZE * chunk.TILE_SIZE
        self.surface = pygame.Surface((chunk_pixel_size, chunk_pixel_size)).convert_alpha()
        self._bake()
    
    def _bake(self):
        ref_pos = [
            self.chunk.world_chunk_x * self.chunk.CHUNK_SIZE * self.chunk.TILE_SIZE,
            self.chunk.world_chunk_y * self.chunk.CHUNK_SIZE * self.chunk.TILE_SIZE
            ]

        for tile in self.chunk.static_tiles:
            if tile is not None:
                tile.render(self.surface, ref_pos)
    
    def render(self, window, ref_pos):
        draw_x = self.chunk.world_chunk_x * self.chunk.CHUNK_SIZE * self.chunk.TILE_SIZE - ref_pos[0]
        draw_y = self.chunk.world_chunk_y * self.chunk.CHUNK_SIZE * self.chunk.TILE_SIZE - ref_pos[1]
        window.blit(self.surface, (draw_x, draw_y))

    def update(self):
        pass

    def delete(self):
        pass