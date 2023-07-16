import pygame, random, math
pygame.init()

from Dot import Dot

class NeuronAnimator:
    def __init__(self, window: pygame.Surface):
        self.window = window

        self.windowWidth, self.windowHeight = window.get_size()

        self.timer = 0
        self.spawnInterval = 400

        self.dotList = []

    def generateRandomDots(self):
        self.timer += 1

        if self.timer > self.spawnInterval:
            newDot = Dot(self.window, 0, random.randint(0, self.windowHeight),
                        random.randint(100, 255), random.randint(5, 7))

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

            for dotToCheckDistance in self.dotList:
                # Here we'll use Pythagoras to solve the distance between dots
                distance = math.sqrt( (dot.x - dotToCheckDistance.x) ** 2 + (dot.y - dotToCheckDistance.y) ** 2 )

                if distance < 120:
                    pygame.draw.line(self.window, (128, 176, 255), (dot.x + round(dot.size / 2), dot.y + round(dot.size / 2)), 
                    (dotToCheckDistance.x + round(dotToCheckDistance.size / 2), dotToCheckDistance.y + round(dotToCheckDistance.size / 2)), 1)

    def run(self):
        self.generateRandomDots()