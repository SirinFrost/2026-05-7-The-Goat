from handlers.particle_handler import ParticleHandler
from handlers.triangle_particle_handler import TriangleParticleHandler
from scripts.components.state import State
import random
import math

class SpawnSquare(State):
    def __init__(self, name):
        super().__init__(name)
        

    def update(self):
        cx, cy = self.entity.rect.center
        self.entity.particle_handler.add_particle(
            cx, cy,
            2, (255, 0, 0),
            random.randint(-100, 100), random.randint(-100, 100),
            1.0,
        )
    

class SpawnTriangle(State):
    def update(self):
        cx, cy = self.entity.rect.center
        self.entity.triangle_particle_handler.add_particle(
            cx, cy,
            2, (0, 255, 0),
            random.randint(-100, 100), random.randint(-100, 100),
            1.0,
            angle=random.uniform(0, math.tau),
            angular_velocity=random.uniform(-4, 4),
        )
