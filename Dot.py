import pygame
pygame.init()

class Dot(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface, x, y, opacity, size) -> None:
        self.x = x
        self.y = y
        self.opacity = opacity
        self.size = size

        self.window = window

        self.velocity = pygame.Vector2(0, 0)
        
        self.image = pygame.image.load("data/dot.png")
        
        self.image.convert()
        self.image.convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.image.set_alpha(opacity)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def render(self):
        self.window.blit(self.image, (self.x, self.y))