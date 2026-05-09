import pygame
import math


pygame.init()



def create_window():
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=True)
    return window

def game_loop(window):
    pygame.display.set_caption("The Goat")
    running = True
    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        window.fill((155, 69, 0))   # clear screen
        # 2. Update
        # (game logic goes here)
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 67, 69), 2)
        pygame.draw.circle(window, (67, 255, 255), (100, 100), 34)
        pygame.draw.ellipse(window, (255, 255, 255), (200, 200, 100, 50), 2)
        pygame.draw.polygon(window, (255, 255, 255), [(720, 720), (690, 634), (720, 790)])
        pygame.draw.line(window, (255, 255, 255), (1080, 720), (555, 555), 2)
        pygame.draw.lines(window, (255, 255, 255), False, [(240, 10), (260, 55), (320, 22)], 2)
        pygame.draw.arc(window, (255, 255, 255), (100, 100, 100, 50), 0, math.pi/2, 2)

    


        # 3. Render

        # (draw calls go here)
        pygame.display.update()

    pygame.quit()


def main():
    window = create_window()
    game_loop(window)

if __name__ == "__main__":
    main()
