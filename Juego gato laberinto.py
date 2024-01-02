import pygame

largo_pantalla = 700
ancho_pantalla = 700
size = (alto_pantalla, ancho_pantalla)
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

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        