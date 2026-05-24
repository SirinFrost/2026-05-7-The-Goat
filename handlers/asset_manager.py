import pygame


class AssetManager:
    def __init__(self):
        self._cache = {}
    
    def get_image(self, path):
        if path not in self._cache:
            self._cache[path] = pygame.image.load(path).convert_alpha()
        return self._cache[path]
