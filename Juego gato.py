import pygame
pygame.init()

LARGO_PANTALLA = 800
ALTO_PANTALLA = 500

#COLORES
brown = (167, 90, 74)
AZUL = (0, 0, 255)

#PERSONAJE PRINCIPAL
class Protagonista(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        pygame.sprite.Sprite.__init__(self)
        
        
        self.image = pygame.image.load('catder.png')
        self.image =  pygame.transform.scale(self.image, (50, 35))
        self.rect = self.image.get_rect()
        
        self.cambio_x = 0
        self.cambio_y = 0
        self.nivel = None
        
    def update(self): 
        #GRAVEDAD
        self.calc_grav()

        self.rect.x += self.cambio_x
         
        #IMPACTOS
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                self.rect.left = bloque.rect.right
                
        self.rect.y += self.cambio_y

        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
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
 
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height
 
    def saltar(self):
         
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
         

        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
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
        pantalla.fill(AZUL)
                
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)
         
    def escenario_desplazar(self, desplazar_x):
        self.desplazar_escenario += desplazar_x

        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x
             
        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x
            
class Nivel_01(Nivel):
 
    def __init__(self, protagonista):
        Nivel.__init__(self, protagonista)
 
        self.limitedel_nivel = -1000
        nivel = [ [210, 70, 500, 500],
                  [210, 70, 800, 400],
                  [210, 70, 1000, 500],
                  [210, 70, 1120, 280],
                  ]
         
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)                      
 

class Nivel_02(Nivel):
 
    def __init__(self, protagonista):
        Nivel.__init__(self, protagonista)
 
        self.limitedel_nivel = -1000
        nivel = [ [210, 30, 450, 570],
                  [210, 30, 850, 420],
                  [210, 30, 1000, 520],
                  [210, 30, 1120, 280],
                  ]
         
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)
 
def main():
    """ Programa Principal """
    pygame.init() 
        
 
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA] 
    pantalla = pygame.display.set_mode(dimensiones) 
       
    pygame.display.set_caption("Side-scrolling Plataformer") 
     

    protagonista = Protagonista()
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))
    listade_niveles.append(Nivel_02(protagonista))

    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
     
    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
     
    protagonista.rect.x = 340
    protagonista.rect.y = ALTO_PANTALLA - protagonista.rect.height
    listade_sprites_activas.add(protagonista)
    
    hecho = False

    reloj = pygame.time.Clock() 
    
    while not hecho: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
     
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
  
        listade_sprites_activas.update()
         
        nivel_actual.update()
         
        if protagonista.rect.x >= 500:
            diff = protagonista.rect.x - 500
            protagonista.rect.x = 500
            nivel_actual.escenario_desplazar(-diff)
     

        if protagonista.rect.x <= 120:
            diff = 120 - protagonista.rect.x
            protagonista.rect.x = 120
            nivel_actual.escenario_desplazar(diff)
  
        posicion_actual = protagonista.rect.x + nivel_actual.desplazar_escenario
        if posicion_actual < nivel_actual.limitedel_nivel:
            protagonista.rect.x = 120
            if nivel_actual_no < len(listade_niveles)-1:
                nivel_actual_no += 1
                nivel_actual = listade_niveles[nivel_actual_no]
                protagonista.nivel = nivel_actual
             
        nivel_actual.draw(pantalla)
        listade_sprites_activas.draw(pantalla)
         
        reloj.tick(60) 
        
        pygame.display.flip() 
    
    pygame.quit()
 
if __name__ == "__main__":
    main()