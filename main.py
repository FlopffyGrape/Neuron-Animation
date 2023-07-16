import pygame

from NeuronAnimator import NeuronAnimator

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Neuron Animation")

clock = pygame.time.Clock()

neuronAnimator = NeuronAnimator(window, clock)

running = True
while running:
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    neuronAnimator.run()

    pygame.display.update()

    clock.tick()

pygame.quit()
quit()
