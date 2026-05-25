import pygame

class Chunk:
    def __init__(self, world_chunk_x, world_chunk_y, CHUNK_SIZE):
        self.world_chunk_x = world_chunk_x
        self.world_chunk_y = world_chunk_y
        self.CHUNK_SIZE = CHUNK_SIZE
        self.id = f"{world_chunk_x}_{world_chunk_y}"
        self.static_tiles = [None] * CHUNK_SIZE * CHUNK_SIZE # LIST

    def add_tile(self, tile):
        index = tile.chunk_y * self.CHUNK_SIZE + tile.chunk_x # col = x, row = y
        self.static_tiles[index] = tile
    
    def update(self):
        pass
    
    def render(self, window, ref_pos):
        for tile in self.static_tiles:
            if tile is not None:
                tile.render(window, ref_pos)