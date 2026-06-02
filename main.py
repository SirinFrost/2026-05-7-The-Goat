import pygame
import math
import random

from entities.hunned_squares import HunnedSquares
from handlers.world import World
from scripts.world.level_loader import LevelLoader
from handlers.particle_handler import ParticleHandler


pygame.init()



def game_loop(world):
    running = True

    # Changing Values here
    x_velocity = 0
    y_velocity = 0



    level_loader = LevelLoader(world, "assets/levels/level_01.json")

    frame_width, frame_height = world.window_handler.frame_size

    #player = Player(680, 360, 100, 100)
    #entity_handler.add_entity(player)

    # square = Square(680, 360, 100, 100, x_velocity, y_velocity, entity_handler)
    # entity_handler.add_entity(square)

    # 100 random square entities
    # Random Positions
    # Random velocities
    # Random colors
    # for i in range(100):
    #     x_velocity = random.randint(-100, 100)
    #     y_velocity = random.randint(-100, 100)
    #     negtentoten1 = random.randint(-100, 100)
    #     negtentoten2 = random.randint(-100, 100)
    #     random_x = random.randint(100, frame_width)
    #     random_y = random.randint(100, frame_height)
    #     randomsize = random.randint(10, 100)
    #     rand_square = HunnedSquares(random_x - randomsize, random_y - randomsize, randomsize, randomsize, negtentoten1, negtentoten2, world.entity_handler)
    #     world.entity_handler.add_entity(rand_square)

    while running:
        running = world.run()

    pygame.quit()


def main():
    world = World()
    game_loop(world)


if __name__ == "__main__":
    main()
