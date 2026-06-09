class EntityHandler:
    def __init__(self, world):
        self.world = world
        self.entities = {}

    def update(self):
        # Iterate a snapshot so an entity that removes itself this frame
        # (e.g. an expired projectile) can't mutate the dict mid-loop.
        for entity in list(self.entities.values()):
            entity.update()
        self.remove_dead()

    def remove_dead(self):
        dead_ids = [
            entity_id
            for entity_id, entity in self.entities.items()
            if getattr(entity, "dead", False)
        ]
        for entity_id in dead_ids:
            self.kill_entity(entity_id)

    def render(self, window, ref_pos):
        for entity in self.entities.values():
            entity.render(window, ref_pos)

    def add_entity(self, entity):
        self.entities[entity.id] = entity
        entity.handler = self

    def remove_entity(self, entity_id):
        del self.entities[entity_id]

    def kill_entity(self, entity_id):
        entity = self.entities[entity_id]
        entity.delete()
        del self.entities[entity_id]
