import pygame

from entities.entity import Entity
from scripts.components.collider_component import ColliderComponent
from scripts.components.spawn import SpawnSquare, SpawnTriangle
from scripts.components.state_handler import StateHandler
from scripts.scenes.scene import Scene
from scripts.world.level_loader import LevelLoader

from entities.square import Square

class PlayScene(Scene):
    def __init__(self):
        super().__init__("play")
        self.state_handler = None

    def enter(self):
        """Runs each time you switch menu → play. Reset world, then set up level."""
        world = self.world

        world.chunks.clear()
        world.entity_handler.entities.clear()
        world.particle_handler.particles.clear()
        world.triangle_particle_handler.particles.clear()

        LevelLoader(world, "assets/levels/level_01.json")



        spawner = Entity(0, 0, 100, 100, 0, 0, world.entity_handler)
        world.entity_handler.add_entity(spawner)
        
        square = Square(0, 0, 100, 100, 0, 0, world.entity_handler)
        world.entity_handler.add_entity(square)
        
        spawner.particle_handler = world.particle_handler
        spawner.triangle_particle_handler = world.triangle_particle_handler

        sh = StateHandler()
        sh.add_state(SpawnSquare("normal"))
        sh.add_state(SpawnTriangle("triangle"))
        spawner.add_component(sh)
        self.state_handler = sh

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_SPACE:
            sh = self.state_handler
            sh.set_state(
                "triangle" if sh.current_state == "normal" else "normal"
            )
        elif event.key == pygame.K_ESCAPE:
            self.manager.set_scene("menu")

    def update(self):
        world = self.world
        world.entity_handler.update()
        for entity in world.entity_handler.entities.values():
            if entity.get_component(ColliderComponent) is not None:
                world.physics_handler.handle_wall_collision(entity)
        world.physics_handler.update()
        world.particle_handler.update()
        world.triangle_particle_handler.update()

    def render(self, frame_buffer):
        world = self.world
        frame_buffer.fill((2, 69, 0))

        for chunk in world.chunks.values():
            chunk.render(frame_buffer, (0, 0))

        world.entity_handler.render(frame_buffer, (0, 0))
        world.particle_handler.render(frame_buffer, (0, 0))
        world.triangle_particle_handler.render(frame_buffer, (0, 0))