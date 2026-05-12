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

    entity_handler = EntityHandler()

    player = Player(680, 360, 100, 100)
    entity_handler.add_entity(player)

    square = Entity(680, 360, 100, 100)
    entity_handler.add_entity(square)

    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= player.speed
        if keys[pygame.K_d]:
            player.x += player.speed
        if keys[pygame.K_w]:
            player.y -= player.speed
        if keys[pygame.K_s]:
            player.y += player.speed

        player.rect.x = player.x
        player.rect.y = player.y

        # Anything being drawn on the screen goes AFTER FILLING THE SCREEN
        window.fill((155, 69, 0))   # clear screen
        # 2. Update
        # (game logic goes here)
        pygame.draw.rect(window, player.color, player.rect)
        
        # Draw shapes


        pygame.draw.rect(window, player.color, player.rect)
        
        # Draw shapes

        pygame.display.flip()

    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
