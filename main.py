import pygame
import math
import random

from entities.entity import Entity
from handlers.entity_handler import EntityHandler
from entities.square import Square
from entities.hunned_squares import HunnedSquares
from handlers.physics_handler import PhysicsHandler
from handlers.asset_manager import AssetManager
from handlers.window_handler import WindowHandler
from handlers.world import World

pygame.init()



def game_loop(world):
    running = True

    # Changing Values here
    x_velocity = 0
    y_velocity = 0

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
        random0to1280 = random.randint(100, 1280)
        random0to720 = random.randint(100, 720)
        randomsize = random.randint(10, 100)
        rand_square = HunnedSquares(random0to1280 - randomsize, random0to720 - randomsize, randomsize, randomsize, negtentoten1, negtentoten2, world.entity_handler)
        world.entity_handler.add_entity(rand_square)

    while running:
        running = world.run()

    pygame.quit()


def main():
    world = World()
    game_loop(world)


if __name__ == "__main__":
    main()
