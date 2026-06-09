import pygame

from scripts.scenes.scene import Scene


class ShopScene(Scene):
    """A menu-style scene for spending money on ship upgrades. It's a sibling of the
    play scene in the FSM: while it's active, PlayScene.update() doesn't run, so opening
    the shop naturally pauses the game — no separate pause flag needed."""

    def __init__(self):
        super().__init__("shop")
        self.selected = 0  # index into world.upgrades.all()

    def enter(self):
        self._title_font = pygame.font.SysFont(None, 44)
        self._row_font = pygame.font.SysFont(None, 28)
        self._hint_font = pygame.font.SysFont(None, 22)
        self.selected = 0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_p, pygame.K_ESCAPE):
            self.manager.set_scene("play")  # resume the (still-intact) game
            return

        options = self.world.upgrades.all()
        if event.key in (pygame.K_UP, pygame.K_w):
            self.selected = (self.selected - 1) % len(options)
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected = (self.selected + 1) % len(options)
        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self._buy(options[self.selected])

    def _buy(self, upgrade):
        if upgrade.maxed:
            return
        if self.world.money >= upgrade.cost:
            self.world.money -= upgrade.cost
            upgrade.level += 1

    def update(self):
        pass

    def render(self, frame_buffer):
        frame_buffer.fill((18, 18, 28))
        w, h = frame_buffer.get_size()

        title = self._title_font.render("SHOP", True, (240, 240, 240))
        frame_buffer.blit(title, title.get_rect(center=(w // 2, 36)))

        money = self._row_font.render(
            f"Money: ${self.world.money}", True, (240, 220, 120)
        )
        frame_buffer.blit(money, money.get_rect(center=(w // 2, 72)))

        options = self.world.upgrades.all()
        row_y = 110
        for i, up in enumerate(options):
            selected = i == self.selected

            if up.maxed:
                price = "MAX"
            elif self.world.money >= up.cost:
                price = f"${up.cost}"
            else:
                price = f"${up.cost} (need more)"

            label = f"{up.name}   Lv {up.level}/{up.max_level}   {price}"

            if selected:
                color = (120, 220, 140)
                # A caret marks the current selection.
                label = "> " + label
            else:
                color = (200, 200, 200)

            text = self._row_font.render(label, True, color)
            frame_buffer.blit(text, (w // 2 - 150, row_y))
            row_y += 34

        hint = self._hint_font.render(
            "Up/Down: select    Enter: buy    P/Esc: back to game",
            True,
            (150, 150, 160),
        )
        frame_buffer.blit(hint, hint.get_rect(center=(w // 2, h - 24)))
