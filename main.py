import pygame
import math
import random

from entities.hunned_squares import HunnedSquares
from handlers.world import World
from scripts.world.tile import Tile
from scripts.world.chunk import Chunk

pygame.init()



def game_loop(world):
    running = True

    # Changing Values here
    x_velocity = 0
    y_velocity = 0

    TILE_SIZE = 16
    CHUNK_SIZE = 16

    chunk = Chunk(0, 0, CHUNK_SIZE)
    
    water = world.asset_manager.get_image("assets/ship_game/water.png")
    water_tile = Tile(0, 0, water, TILE_SIZE)
    
    for row in range(CHUNK_SIZE):
        for col in range(CHUNK_SIZE):
            tile = Tile(col, row, water, TILE_SIZE)
            chunk.add_tile(tile)

    world.chunks[f"0_0"] = chunk

    frame_width, frame_height = world.window_handler.frame_size

    #player = Player(680, 360, 100, 100)
    #entity_handler.add_entity(player)

    # square = Square(680, 360, 100, 100, x_velocity, y_velocity, entity_handler)
    # entity_handler.add_entity(square)

    # 100 random square entities
    # Random Positions
    # Random velocities
    # Random colors
    for i in range(100):
        x_velocity = random.randint(-10, 10)
        y_velocity = random.randint(-10, 10)
        negtentoten1 = random.randint(-10, 10)
        negtentoten2 = random.randint(-10, 10)
        random_x = random.randint(100, frame_width)
        random_y = random.randint(100, frame_height)
        randomsize = random.randint(10, 100)
        rand_square = HunnedSquares(random_x - randomsize, random_y - randomsize, randomsize, randomsize, negtentoten1, negtentoten2, world.entity_handler)
        world.entity_handler.add_entity(rand_square)

    while running:
        running = world.run()

    pygame.quit()


def main():
    world = World()
    game_loop(world)


if __name__ == "__main__":
    main()
