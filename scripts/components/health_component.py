from scripts.components.component import Component


class HealthComponent(Component):
    """Tracks hit points. When HP runs out it tells its entity to delete() itself —
    the entity decides what 'delete' means (e.g. flag dead for the EntityHandler sweep)."""

    def __init__(self, hp=3):
        super().__init__()
        self.max_hp = hp
        self.hp = hp

    def take_damage(self, amount=1):
        if self.hp <= 0:
            return
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.entity.delete()
