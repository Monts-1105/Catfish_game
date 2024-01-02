import pygame
pygame.init()

largo = 800
alto = 500
size = (largo,  alto)
screen = pygame.display.set_mode(size)

#COLORES
white = (255, 255, 255)
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)
gray_light = (200, 200, 200)
gray_dark = (50, 50, 50)
blue_light  = (170, 200, 255)
brown = (167, 90, 74)

#CLASE PERSONAJE PRINCIPAL

#IMAGENES SUBIDAS
background = pygame.image.load('sky.png')
background = pygame.transform.scale(background, (900, 500))
#SOL
sun = pygame.image.load('sun.png')
sun = pygame.transform.scale(sun, (100, 100))
#NUBES
cloud1 = pygame.image.load('nube2.png')
cloud1 = pygame.transform.scale(cloud1, (150, 100))
cloud2 = pygame.image.load('nube1.png')
cloud2 = pygame.transform.scale(cloud2, (150, 100))
cloud3 = pygame.image.load('nube3.png')
cloud3 = pygame.transform.scale(cloud3, (150, 100))
cloud4 = pygame.image.load('nube4.png')
cloud4 = pygame.transform.scale(cloud4, (150, 100))
cloud5 = pygame.image.load('nube5.png')
cloud5 = pygame.transform.scale(cloud5, (200, 120))
#BLOQUES DE PASTO
bloqpast1 = pygame.image.load('pasto.jpg')
bloqpast1 = pygame.transform.scale(bloqpast1, (50, 40))
#GATO
cat = pygame.image.load('catder.png')
cat = pygame.transform.scale(cat, (50, 35))

#SPRITES
nivel = None


#FPS
reloj = pygame.time.Clock()

#COORDENADAS DEL PERSONAJE
cordex = 10
cordey = 290
#VELOCIDAD
velx = 0
vely = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #EVENTOS TECLADO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velx = -3
            if event.key == pygame.K_RIGHT:
                velx = 3
            if event.key == pygame.K_UP:
                vely = 0
            if event.key == pygame.K_DOWN:
                vely = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velx = 0
            if event.key == pygame.K_RIGHT:
                velx = 0
            if event.key == pygame.K_UP:
                vely = -3
            if event.key == pygame.K_DOWN:
                vely = 3
        
        cordex += velx
        
        
        
        #UBICACIONES DE IMAGENES
        screen.blit(background, (0, 0))
        #PERSONAJE
        screen.blit(cat, (cordex, cordey))
        #SOL
        screen.blit(sun, (350, 10))
        #NUBES
        screen.blit(cloud1, (50, 10))
        screen.blit(cloud2, (140, 30))
        screen.blit(cloud5, (550, 25))
        #BLOQUES DE PASTO
        screen.blit(bloqpast1, (0, 350))
        screen.blit(bloqpast1, (65, 350))
        screen.blit(bloqpast1, (195, 350))
        screen.blit(bloqpast1, (325, 220))
        screen.blit(bloqpast1, (390, 220))
        screen.blit(bloqpast1, (520, 350))
        screen.blit(bloqpast1, (650, 350))
        pygame.display.flip()
pygame.quit()
