import pygame
import math

from entities.entity import Entity
from handlers.entity_handler import EntityHandler
from entities.square import Square



pygame.init()



def create_window():
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=True)
    return window

def game_loop(window):
    pygame.display.set_caption("The Goat")
    running = True

    entity_handler = EntityHandler()

    #player = Player(680, 360, 100, 100)
    #entity_handler.add_entity(player)

    square = Square(680, 360, 100, 100)
    entity_handler.add_entity(square)

    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        square.rect.x = square.x
        square.rect.y = square.y

        # Anything being drawn on the screen goes AFTER FILLING THE SCREEN
        window.fill((155, 69, 0))   # clear screen
        # 2. Update
        # (game logic goes here)
        # Draw shapes


        entity_handler.update()
        
        # Draw shapes
        pygame.draw.rect(window, square.color, square.rect)

        #update window
        pygame.display.flip()
    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
