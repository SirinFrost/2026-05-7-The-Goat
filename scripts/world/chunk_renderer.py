import pygame

class ChunkRenderer:
    def __init__(self, chunk, tile_size):
        self.chunk = chunk
        self.tile_size = tile_size
        chunk_pixel_size = chunk.CHUNK_SIZE * tile_size
        self.surface = pygame.Surface((chunk_pixel_size, chunk_pixel_size)).convert_alpha()
        self._bake()
    
    def _bake(self):
        for tile in self.chunk.static_tiles:
            if tile is not None:
                self.surface.blit(tile.image, (tile.chunk_x * self.tile_size, tile.chunk_y * self.tile_size))
    
    def render(self, window, ref_pos):
        draw_x = self.chunk.world_chunk_x * self.chunk.CHUNK_SIZE * self.tile_size - ref_pos[0]
        draw_y = self.chunk.world_chunk_y * self.chunk.CHUNK_SIZE * self.tile_size - ref_pos[1]
        window.blit(self.surface, (draw_x, draw_y))

    def update(self):
        pass

    def delete(self):
        pass