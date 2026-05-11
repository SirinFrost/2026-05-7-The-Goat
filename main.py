import pygame
import math

from entities.entity import Entity
from handlers.entity_handler import EntityHandler

from player import Player


pygame.init()



def create_window():
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=True)
    return window

def game_loop(window):
    pygame.display.set_caption("The Goat")
    running = True

    player = Player(680, 360, 100, 100)
    entity_handler = EntityHandler()
    entity_handler.add_entity(player)

    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        window.fill((155, 69, 0))   # clear screen
        # 2. Update
        # (game logic goes here)

        pygame.draw.rect(window, player.color, player.rect)
        
        # Draw shapes

    


        # 3. Render

        # (draw calls go here)
        pygame.display.update()

    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
