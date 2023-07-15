import pygame

from NeuronAnimator import NeuronAnimator

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Neuron Animation")

neuronAnimator = NeuronAnimator(window, window.get_width(), window.get_height())

running = True
while running:
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    neuronAnimator.run()

    pygame.display.update()

pygame.quit()
quit()
