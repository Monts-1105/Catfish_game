import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)
gray_light = (200, 200, 200)
gray_dark = (50, 50, 50)
blue_light  = (170, 200, 255)

size = 800, 600
ventana = pygame.display.set_mode(size)
ventana.fill(blue_light)
pygame.display.set_caption("Mi primer pygame")
pygame.draw.line(ventana, white,(20, 20), (400, 400), 5)
pygame.draw.circle(ventana, red, (400, 200), 100, 1)
pygame.draw.rect(ventana, green, pygame.Rect(400, 20, 50, 100), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        pygame.display.flip()
pygame.quit()