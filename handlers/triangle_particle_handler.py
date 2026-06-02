import math
import pygame
from handlers.particle_handler import ParticleHandler




class TriangleParticleHandler(ParticleHandler):
    def render(self, window, ref_pos):
        ref_x, ref_y = ref_pos[0], ref_pos[1]

        for particle in self.particles:
            cx = particle["x"] - ref_x
            cy = particle["y"] - ref_y
            size = particle["size"]
            pygame.draw.polygon(window, particle["color"], [
                (cx, cy),
                (cx + size, cy),
                (cx, cy + size)
            ])

    def add_particle(self, x, y, size, color, vx, vy, lifetime=1.0,
                    angle=0.0, angular_velocity=0.0):
        self.particles.append({
            "x": x, "y": y, "size": size, "color": color,
            "vx": vx, "vy": vy, "lifetime": lifetime,
            "angle": angle,
            "angular_velocity": angular_velocity,
        })
    
    def update(self):
        alive_particles = []
        dt = self.world.delta_time
        for p in self.particles:
            p["x"] += p["vx"] * dt
            p["y"] += p["vy"] * dt
            p["angle"] += p["angular_velocity"] * dt
            p["lifetime"] -= dt
            if p["lifetime"] > 0:
                alive_particles.append(p)
        self.particles = alive_particles
    
    def _triangle_local_points(self, size):
        return [
            (0, -size),           # tip
            (-size, size),        # bottom left
            (size, size),         # bottom right
        ]

    def _rotate_point(self, x, y, angle):
        c, s = math.cos(angle), math.sin(angle)
        return (x * c - y * s, x * s + y * c)

    def render(self, window, ref_pos):
        ref_x, ref_y = ref_pos[0], ref_pos[1]
        for p in self.particles:
            cx = p["x"] - ref_x
            cy = p["y"] - ref_y
            angle = p["angle"]
            points = []
            for lx, ly in self._triangle_local_points(p["size"]):
                rx, ry = self._rotate_point(lx, ly, angle)
                points.append((cx + rx, cy + ry))
            pygame.draw.polygon(window, p["color"], points)