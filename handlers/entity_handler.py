class EntityHandler:
    def __init__(self):
        self.entities = {}
    
    def update(self):
        for entity in self.entities.values():
            entity.update()

    def render(self, window, ref_pos):
        for entity in self.entities.values():
            entity.render(window, ref_pos)

    def add_entity(self, entity):
        self.entities[entity.id] = entity

    def remove_entity(self, entity_id):
        del self.entities[entity_id]

    def kill_entity(self, entity_id):
        entity = self.entities[entity_id]
        entity.delete()
        del self.entities[entity_id]