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
        self.rect.y += 1
        
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
        self.vel_x = 0
        self.vel_y = 0
        
    def changesspeed(self, x, y):
        self.vel_x += x
        self.vel_y += y
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


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
background_music = pygame.mixer.Sound('Background_music.mp3')
pygame.mixer.music.load('Background_music.mp3')
pygame.mixer.music.play(-1)
collect_sound = pygame.mixer.Sound('Drop_sound.mp3')

time_elapsed = 0
    
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat.changesspeed(-3, 0)
            if event.key == pygame.K_RIGHT:
                cat.changesspeed(3, 0)
            if event.key == pygame.K_UP:
                cat.changesspeed(0, -3)
            if event.key == pygame.K_DOWN:
                cat.changesspeed(0, 3)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.changesspeed(3, 0)
            if event.key == pygame.K_RIGHT:
                cat.changesspeed(-3, 0)
            if event.key == pygame.K_UP:
                cat.changesspeed(0, 3)
            if event.key == pygame.K_DOWN:
                cat.changesspeed(0, -3)
            
            
    lista_todos_los_sprites.update()
        
    fish_lista_completa = pygame.sprite.spritecollide(cat, fish_lista, True)
    
    for fish in fish_lista:
        score += 1
        print(score)
        collect_sound.play()
            
        
    screen.blit(background, [0, 0])
    
    lista_todos_los_sprites.draw(screen)
            
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()