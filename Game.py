import pygame
pygame.init()

largopant = 800
altopant = 500
altura = 65
anchura = 60

#COLORES
white = (255, 255, 255)
red = (255, 0, 0)
green = ( 0, 255, 0)
blue = ( 0, 0, 255)
gray_light = (200, 200, 200)
gray_dark = (50, 50, 50)
blue_light  = (170, 200, 255)
brown = (167, 90, 74)

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
bloqpast1 = pygame.transform.scale(bloqpast1, (65, 60))
#GATO
cat = pygame.image.load('catder.png')
cat = pygame.transform.scale(cat, (50, 35))


#CLASE PERSONAJE PRINCIPAL
class Personaje(pygame.sprite.Sprite):
    
    #METODOS
    def __init__(self):
        super().__init__() 
        pygame.sprite.Sprite.__init__(self)
 
        #FIGURA
        
        self.image = pygame.image.load('catder.png')
        self.image =  pygame.transform.scale(self.image, (50, 35))
        self.rect = self.image.get_rect()
        
        #VELOCIDAD DEL PERSONAJE
        self.cambio_x = 0
        self.cambio_y = 0
        self.level = None

    def update(self): 
        #GRAVEDAD
        self.calc_grav()
         
        #IZQUIERDA DERECHA
        self.rect.x += self.cambio_x
         
        #COMPROBAR CHOQUE CON OBJETOS
        impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in impactos_bloques:
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                self.rect.left = bloque.rect.right
 
        #ARRIBA IZQUIERDA
        self.rect.y += self.cambio_y
         
        #COMPROBAR CHOQUE CON OBJETOS
        impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in impactos_bloques:
 
            #RESTABLECER POSICIÓN
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
 
            #DETENER MOVIMIENTO VERTICAL
            self.cambio_y = 0
 
    def calc_grav(self):
        #CALCULO DE GRAVEDAD
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
 
        if self.rect.y >= altopant - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = altopant - self.rect.height
 
    def saltar(self):

        #BOTON DE SALTAR
        self.rect.y += 2
        impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
         
        if len(impactos_plataforma) > 0 or self.rect.bottom >= altopant:
            self.cambio_y = -10
             
    #MOVIMIENTO
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
         
        # Cuán lejos se ha desplazado a la izquierda/derecha el escenario
        self.desplazar_escenario = 0


    # Actualizamos todo en este nivel
    def update(self):
        """ Actualizamos todo en este nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()
     
    def draw(self, pantalla):
        """ Dibujamos todo en este nivel. """
         
        # Dibujamos el fondo
        pantalla.blit(background, (0, 0))
                   
        # Dibujamos todas las listas de sprites que tengamos
        self.listade_plataformas.draw(background)
        self.listade_enemigos.draw(background)
         
    def escenario_desplazar(self, desplazar_x):
        """ Para cuando el usuario se desplaza a la izquierda/derecha y necesitamos mover 
        todo: """
         
        # Llevamos la cuenta de la cantidad de desplamiento
        self.desplazar_escenario += desplazar_x
         
        # Iteramos a través de todas las listas de sprites y desplazamos
        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x
             
        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x
            
# Creamos las plataformas para el nivel
class Nivel_01(Nivel):
    """ Definición para el nivel 1. """
 
    def __init__(self, protagonista):
        """ Creamos el nivel 1. """
         
        # Llamamos al constructor padre
        Nivel.__init__(self, protagonista)
 
        self.limitedel_nivel = -1000
         
        # Array con el largo, alto, x, e y de la plataforma
        nivel = [ [65, 30, 0, 350],
                  [65, 60, 50, 350],
                  [65, 60, 150, 350],
                  [65, 60, 250, 220],
                  ]
         
         
        # Iteramos a través del array anterior y añadimos plataformas
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
 
# Creamos las plataformas para el nivel
class Nivel_02(Nivel):
    """ Definición para el nivel 2. """
 
    def __init__(self, protagonista):
        """ Creamos el nivel 1. """
         
        # Llamamos al constructor padre
        Nivel.__init__(self, protagonista)
 
        self.limitedel_nivel = -1000
         
        # Array con el largo, alto, x, e y de la plataforma
        nivel = [ [65, 60, 0, 350],
                  [65, 60, 65, 350],
                  [65, 60, 195, 350],
                  [65, 60, 325, 220],
                  ]
         
         
        # Iteramos a través del array anterior y añadimos plataformas
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
    """ Programa Principal """
    pygame.init() 
    
    #PANTALLA
    size = (largopant,  altopant)
    screen = pygame.display.set_mode(size)    
       
    pygame.display.set_caption("Side-scrolling Plataformer") 
     
    # Creamos al protagonista
    protagonista = Personaje()
 
    # Creamos todos los niveles
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))
    listade_niveles.append(Nivel_02(protagonista))
     
    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
     
    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
     
    protagonista.rect.x = 340
    protagonista.rect.y = altopant - protagonista.rect.height
    listade_sprites_activas.add(protagonista)
         
    #Iteramos hasta que el usuario hace click sobre el botón de salir. 
    hecho = False
       
    # Usado para gestionar cuán rápido se actualiza la pantalla.
    reloj = pygame.time.Clock() 
       
    # -------- Bucle Principal del Programa  ----------- 
    while not hecho: 
        for evento in pygame.event.get(): # El usuario realizó alguna acción 
            if evento.type == pygame.QUIT: #Si el usuario hizo click en salir
                hecho = True # Marcamos como hecho y salimos de este bucle
     
                #SOL
                screen.blit(sun, (350, 10))
                #NUBES
                screen.blit(cloud1, (50, 10))
                screen.blit(cloud2, (140, 30))
                screen.blit(cloud5, (550, 25))
     
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if evento.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if evento.key == pygame.K_UP:
                    protagonista.saltar()
                     
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and protagonista.cambio_x < 0: 
                    protagonista.stop()
                if evento.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()
 
        # Actualizamos al protagonista. 
        listade_sprites_activas.update()
         
        # Actualizamos los objetos en el nivel
        nivel_actual.update()
         
        # Si el protagonista se aproxima al borde derecho, desplazamos el escenario a la izquierda(-x)
        if protagonista.rect.x >= 500:
            diff = protagonista.rect.x - 500
            protagonista.rect.x = 500
            nivel_actual.escenario_desplazar(-diff)
     
        # Si el protagonista se aproxima al borde izquierdo, desplazamos el escenario a la derecha(+x)
        if protagonista.rect.x <= 120:
            diff = 120 - protagonista.rect.x
            protagonista.rect.x = 120
            nivel_actual.escenario_desplazar(diff)
  
        # Si el protagonista alcanza el final del nivel, pasa al siguiente
        posicion_actual = protagonista.rect.x + nivel_actual.desplazar_escenario
        if posicion_actual < nivel_actual.limitedel_nivel:
            protagonista.rect.x = 120
            if nivel_actual_no < len(listade_niveles)-1:
                nivel_actual_no += 1
                nivel_actual = listade_niveles[nivel_actual_no]
                protagonista.nivel = nivel_actual
             
        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
        nivel_actual.draw(screen)
        listade_sprites_activas.draw(screen)
         
        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
           
        # Limitamos a 60 fps
        reloj.tick(60) 
       
        # Avanzamos y actualizamos la pantalla que ya hemos dibujado 
        pygame.display.flip() 
           
    # Pórtate bien con el IDLE. Si olvidas esta línea, el programa se 'colgará' 
    # al salir.
    pygame.quit()
 
if __name__ == "__main__":
    main()