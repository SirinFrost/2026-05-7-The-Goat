import pygame
import math


pygame.init()



def create_window():
    window = pygame.display.set_mode((800, 600), pygame.RESIZABLE, vsync=True)
    return window

def game_loop(window):
    running = True
    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # 2. Update
        # (game logic goes here)



        # 3. Render
        window.fill((155, 69, 0))   # clear screen
        # (draw calls go here)
        pygame.display.update()

    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
