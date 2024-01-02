import pygame

pygame.init()

largopant = 800
altopant = 500

# COLORES
white = (255, 255, 255)

# IMÁGENES SUBIDAS
background = pygame.image.load('sky.png')
background = pygame.transform.scale(background, (900, 500))

sun = pygame.image.load('sun.png')
sun = pygame.transform.scale(sun, (100, 100))

cloud1 = pygame.image.load('nube2.png')
cloud1 = pygame.transform.scale(cloud1, (150, 100))
cloud2 = pygame.image.load('nube1.png')
cloud2 = pygame.transform.scale(cloud2, (150, 100))
cloud5 = pygame.image.load('nube5.png')
cloud5 = pygame.transform.scale(cloud5, (200, 120))

bloqpast1 = pygame.image.load('pasto.jpg')
bloqpast1 = pygame.transform.scale(bloqpast1, (50, 40))

cat = pygame.image.load('catder.png')
cat = pygame.transform.scale(cat, (50, 35))


class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('catder.png')
        self.image = pygame.transform.scale(self.image, (50, 35))
        self.rect = self.image.get_rect()
        self.cambio_x = 0
        self.cambio_y = 0
        self.level = None

    def update(self):
        self.calc_grav()
        self.rect.x += self.cambio_x
        impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in impactos_bloques:
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                self.rect.left = bloque.rect.right

        self.rect.y += self.cambio_y
        impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in impactos_bloques:
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
            self.cambio_y = 0

    def calc_grav(self):
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
        if self.rect.y >= altopant - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = altopant - self.rect.height

    def saltar(self):
        self.rect.y += 2
        impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
        if len(impactos_plataforma) > 0 or self.rect.bottom >= altopant:
            self.cambio_y = -10

    def ir_izquierda(self):
        self.cambio_x = -6

    def ir_derecha(self):
        self.cambio_x = 6

    def stop(self):
        self.cambio_x = 0


class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pasto.jpg')
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()


class Nivel():
    def __init__(self, protagonista):
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
        self.desplazar_escenario = 0

    def update(self):
        self.listade_plataformas.update()
        self.listade_enemigos.update()

    def draw(self, pantalla):
        pantalla.blit(background, (0, 0))
        pantalla.blit(sun, (350, 10))
        pantalla.blit(cloud1, (50, 10))
        pantalla.blit(cloud2, (140, 30))
        pantalla.blit(cloud5, (550, 25))
        self.listade_plataformas.draw(background)
        self.listade_enemigos.draw(background)

    def escenario_desplazar(self, desplazar_x):
        self.desplazar_escenario += desplazar_x
        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x
        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x


class Nivel_01(Nivel):
    def __init__(self, protagonista):
        Nivel.__init__(self, protagonista)
        self.limitedel_nivel = 800
        nivel = [
            [65, 30, 0, 350],
            [65, 60, 50, 350],
            [65, 60, 150, 350],
            [65, 60, 250, 220],
        ]
        for plataforma in nivel:
            pasillo = Plataforma()
            bloque = Plataforma()
            pasillo.rect.x = plataforma[0]
            pasillo.rect.y = plataforma[1]
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            pasillo.protagonista = self.protagonista
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(pasillo)
            self.listade_plataformas.add(bloque)


class Nivel_02(Nivel):
    def __init__(self, protagonista):
        Nivel.__init__(self, protagonista)
        self.limitedel_nivel = 800
        nivel = [
            [65, 60, 0, 350],
            [65, 60, 65, 350],
            [65, 60, 195, 350],
            [65, 60, 325, 220],
        ]
        for plataforma in nivel:
            pasillo = Plataforma()
            bloque = Plataforma()
            pasillo.rect.x = plataforma[0]
            pasillo.rect.y = plataforma[1]
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            pasillo.protagonista = self.protagonista
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(pasillo)
            self.listade_plataformas.add(bloque)


def main():
    pygame.init()
    size = (largopant, altopant)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Side-scrolling Plataformer")
    protagonista = Personaje()
    listade_niveles = [Nivel_01(protagonista), Nivel_02(protagonista)]
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
    protagonista.rect.x = nivel_actual.listade_plataformas.sprites()[0].rect.x
    protagonista.rect.y = nivel_actual.listade_plataformas.sprites()[0].rect.y - protagonista.rect.height
    listade_sprites_activas.add(protagonista)
    hecho = False
    reloj = pygame.time.Clock()
    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            protagonista.ir_izquierda()
        if keys[pygame.K_RIGHT]:
            protagonista.ir_derecha()
        if keys[pygame.K_UP]:
            protagonista.saltar()

        listade_sprites_activas.update()
        nivel_actual.update()
        posicion_actual = protagonista.rect.x + nivel_actual.desplazar_escenario
        if posicion_actual < nivel_actual.limitedel_nivel:
            protagonista.rect.x = nivel_actual.listade_plataformas.sprites()[0].rect.x
            protagonista.rect.y = nivel_actual.listade_plataformas.sprites()[0].rect.y - protagonista.rect.height
            if nivel_actual_no < len(listade_niveles) - 1:
                nivel_actual_no += 1
                nivel_actual = listade_niveles[nivel_actual_no]
                protagonista.nivel = nivel_actual

        screen.fill(white)
        nivel_actual.draw(screen)
        listade_sprites_activas.draw(screen)
        reloj.tick(60)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()