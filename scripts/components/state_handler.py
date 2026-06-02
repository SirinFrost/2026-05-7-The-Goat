from scripts.components.component import Component


class StateHandler(Component):
    def __init__(self):
        super().__init__()
        self.states = {}
        self.current_state = None
    
    def add_state(self, state):
        state.handler = self
        self.states[state.name] = state
        if self.current_state is None:
            self.current_state = state.name
    
    def set_state(self, name):
        if name == self.current_state:
            return
        self.states[self.current_state].exit()
        self.current_state = name
        self.states[name].enter()
    
    def update(self):
        self.states[self.current_state].update()