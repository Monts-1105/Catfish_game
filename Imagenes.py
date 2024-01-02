import pygame

pygame.init()
size = 800, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Mi segundo python")

background = pygame.image.load('tingling.jpg')
background = pygame.transform.scale(background, (500, 500))
ming = pygame.image.load('pepitaming.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ventana.blit(background, (100, 50))
        pygame.display.flip()
pygame.quit()
