import pygame, random
pygame.init()

from Dot import Dot
from LineInfo import LineInfo

class NeuronAnimator:
    def __init__(self, window: pygame.Surface, windowWidth, windowHeight):
        self.window = window

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.timer = 0
        self.spawnInterval = 600

        self.dotList = []

    def generateRandomDots(self):
        self.timer += 1

        if self.timer > self.spawnInterval:
            newDot = Dot(self.window, 0, random.randint(0, self.windowHeight), random.randint(100, 255), random.randint(5, 7))

            newDot.velocity.x = random.randint(4, 8)/100
            newDot.velocity.y = random.randint(-2, 2)/100

            self.dotList.append(newDot)
            self.timer = 0

        for dot in self.dotList:
            if (dot.x > self.window.get_width()
            or dot.y > self.window.get_height() or dot.y < 0):
                self.dotList.remove(dot)

            dot.render()
            dot.move()

    def run(self):
        self.generateRandomDots()