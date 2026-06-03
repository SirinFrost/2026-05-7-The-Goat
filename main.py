import pygame
import math
import random

from entities.hunned_squares import HunnedSquares
from handlers.world import World

pygame.init()



def main():
    world = World()
    while world.run():
        pass
    pygame.quit()


if __name__ == "__main__":
    main()
