import pygame
pygame.init()

class Dot(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface, pos, opacity, size) -> None:
        self.pos = pos
        self.opacity = opacity
        self.size = size
        
        self.image = pygame.image.load("data/dot.png").convert()

    def render(self):
        pygame.transform.scale(self.image, (self.size, self.size))
        
        