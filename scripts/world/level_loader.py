import json

from scripts.world.chunk import Chunk
from scripts.world.tile import Tile
from scripts.world.chunk_renderer import ChunkRenderer

class LevelLoader:

    CHUNK_SIZE = 16
    TILE_SIZE = 16

    def __init__(self, world, filepath):
        with open(filepath, "r") as f:
            self.data = json.load(f)
        self.tile_images = self.data["tile_images"]

        for chunk_data in self.data["chunks"]:
            chunk = Chunk(chunk_data["world_chunk_x"], chunk_data["world_chunk_y"], self.CHUNK_SIZE)
            for i, tile_id in enumerate(chunk_data["tiles"]):
                if tile_id is None:
                    continue

                path = self.tile_images[str(tile_id)]
                surface = world.asset_manager.get_image(path)
                chunk.static_tiles[i] = Tile(i % self.CHUNK_SIZE, i // self.CHUNK_SIZE, surface, self.TILE_SIZE)
            chunk_renderer = ChunkRenderer(chunk)
            world.chunks[chunk.id] = chunk_renderer