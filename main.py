import pygame
import math
import random

from entities.entity import Entity
from handlers.entity_handler import EntityHandler
from entities.square import Square
from entities.hunned_squares import HunnedSquares

pygame.init()



def create_window():
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=True)
    return window

def game_loop(window):
    pygame.display.set_caption("The Goat")
    running = True

    clock = pygame.time.Clock()
    timer = 0.0
    # Changing Values here
    x_velocity = 0
    y_velocity = 0

    entity_handler = EntityHandler()

    #player = Player(680, 360, 100, 100)
    #entity_handler.add_entity(player)

    # square = Square(680, 360, 100, 100, x_velocity, y_velocity)
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
        rand_square = HunnedSquares(random0to1280 - randomsize, random0to720 - randomsize, randomsize, randomsize, negtentoten1, negtentoten2)
        entity_handler.add_entity(rand_square)

    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        # Anything being drawn on the screen goes AFTER FILLING THE SCREEN
        window.fill((155, 69, 0))   # clear screen
        # 2. Update
        # (game logic goes here)
        # Draw shapes
        entity_handler.update()
        entity_handler.render(window, (0, 0))

        #update window
        pygame.display.flip()
        # delta time and clock tick
        delta_time = clock.tick(60) / 1000.0
        timer += delta_time
        if timer >= 1.0:
            print(clock.get_fps())
            timer = 0.0

    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
