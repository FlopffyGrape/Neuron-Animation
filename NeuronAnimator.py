import pygame, random
pygame.init()

from Dot import Dot
from LineInfo import LineInfo

class NeuronAnimator:
    def __init__(self, window: pygame.Surface, windowWidth, windowHeight):
        self.window = window

        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dotList = []

    def generateRandomDots(self):
        newDotPos = (0, random.randint(0, self.windowHeight) )
        newDot = Dot(self.window, newDotPos, random.randint(), random.randint(10, 20))
        self.dotList.append()

    def run(self):
        self.generateRandomDots()