import pygame, random

white = (255, 255, 255)
black = (0, 0, 0)

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('fish.png').convert()
        self.image.set_colorkey(black)
        self.image =  pygame.transform.scale(self.image, (60, 45))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 3
        
        if self.rect.y > alto:
            self.rect.y = -10
            self.rect.x = random.randrange(largo)
        
class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('catder.png').convert()
        self.image.set_colorkey(white)
        self.image =  pygame.transform.scale(self.image, (85, 70))
        self.rect = self.image.get_rect()
        
    def update(self):
        posicion_mouse = pygame.mouse.get_pos()
        cat.rect.x = posicion_mouse[0]
        cat.rect.y = posicion_mouse[1]


pygame.init()

largo = 600
alto = 600
size = (largo,  alto)
screen = pygame.display.set_mode(size)

background = pygame.image.load('suelo_pasto.jpg')
clock = pygame.time.Clock()  
done = False
score = 0

fish_lista = pygame.sprite.Group()
lista_todos_los_sprites = pygame.sprite.Group()

for i in range(30):
    fish = Fish()
    fish.rect.x = random.randrange(largo)
    fish.rect.y = random.randrange(alto)
    
    fish_lista.add(fish)
    lista_todos_los_sprites.add(fish)
    
cat = Cat()
lista_todos_los_sprites.add(cat)
sound = pygame.mixer.Sound('Drop_sound.mp3')
    
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    lista_todos_los_sprites.update()
        
    fish_lista_completa = pygame.sprite.spritecollide(cat, fish_lista, True)
    
    for fish in fish_lista:
        score += 1
        print(score)
            
    screen.blit(background, [0, 0])
    
    lista_todos_los_sprites.draw(screen)
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()