import pygame


P_X, P_Y, P_VX, P_VY, P_LIFE = 0,1,2,3,4

class ParticleHandler:
    def __init__(self, world): # world has world.delta_time
        self.world = world
        self.particles = []
    
    def add_particle(self, x, y, size, color, vx, vy, lifetime=1.0):
        self.particles.append({
            "x": x,
            "y": y,
            "size": size,
            "color": color,
            "vx": vx,
            "vy": vy,
            "lifetime": lifetime
        })
    
    def kill_particle(self, x, y):
        for particle in self.particles:
            if particle["x"] == x and particle["y"] == y:
                self.particles.remove(particle)
                break

    def update(self):
        alive_particles = []
        dt = self.world.delta_time
        for particle in self.particles:
            particle["x"] += particle["vx"] * dt
            particle["y"] += particle["vy"] * dt
            particle["lifetime"] -= dt
            if particle["lifetime"] > 0:
                alive_particles.append(particle)
        self.particles = alive_particles

    def render(self, window, ref_pos):
        for particle in self.particles:
            pygame.draw.rect(
                window,
                particle["color"],
                (particle["x"] - ref_pos[0],
                particle["y"] - ref_pos[1],
                particle["size"],
                particle["size"]
                )
            )