from scripts.components.component import Component


class SceneManager(Component):
    def __init__(self, world):
        self.world = world
        self.scenes = {}
        self.current_scene = None
    
    def add_scene(self, scene):
        scene.manager = self
        self.scenes[scene.name] = scene
        if self.current_scene is None:
            self.current_scene = scene.name
            scene.enter()
    
    def set_scene(self, name):
        if name == self.current_scene:
            return
        self.scenes[self.current_scene].exit()
        self.current_scene = name
        self.scenes[name].enter()
    
    def handle_event(self, event):
        self.scenes[self.current_scene].handle_event(event)
    
    def update(self):
        self.scenes[self.current_scene].update()
    
    def render(self, frame_buffer):
        self.scenes[self.current_scene].render(frame_buffer)