class Upgrade:
    """One purchasable stat. Pure data: a level counter plus the rules for turning that
    level into a gameplay value and a price. It knows nothing about ships or the shop —
    behavior reads `value`, the shop reads `cost` and bumps `level`."""

    def __init__(self, name, base, step, cost, cost_growth=1.6, max_level=8):
        self.name = name
        self.base = base  # value at level 0
        self.step = step  # value added per level
        self.level = 0
        self.base_cost = cost  # price of the first level
        self.cost_growth = cost_growth  # each level costs this much more
        self.max_level = max_level

    @property
    def value(self):
        return self.base + self.step * self.level

    @property
    def cost(self):
        return int(self.base_cost * (self.cost_growth ** self.level))

    @property
    def maxed(self):
        return self.level >= self.max_level


class Upgrades:
    """The player's upgrade levels, living on the World so they persist across scenes
    (the shop edits them, the ship reads them). Separating these stats from the ship's
    components means buying an upgrade just changes a number here — no entity rebuilding."""

    def __init__(self):
        self.max_speed = Upgrade("Max Velocity", base=320, step=80, cost=40)
        self.acceleration = Upgrade("Acceleration", base=900, step=220, cost=40)
        self.bullet_speed = Upgrade("Bullet Speed", base=600, step=150, cost=35)
        self.bullet_count = Upgrade("Bullets Fired", base=1, step=1, cost=60, max_level=4)

    def all(self):
        """Ordered list so the shop can show and index them consistently."""
        return [
            self.max_speed,
            self.acceleration,
            self.bullet_speed,
            self.bullet_count,
        ]
