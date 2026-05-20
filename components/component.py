import uuid

class Component:
    def __init__(self):
        self.id = uuid.uuid1()
        self.entity = None
    
    def update(self):
        pass
    
    def render(self, window, ref_pos):
        pass