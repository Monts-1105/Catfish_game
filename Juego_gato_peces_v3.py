import pygame, random

largo = 600
alto = 600
white = (255, 255, 255)
black = (0, 0, 0)

background = pygame.image.load('suelo_pasto.jpg')

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
        
        


class Game(object):
    def __init__(self):
        self.game_over = False
        
        self.score = 0
        
        self.fish_lista = pygame.sprite.Group()
        self.lista_todos_los_sprites = pygame.sprite.Group()
        
        for i in range(30):
            fish = Fish()
            fish.rect.x = random.randrange(largo)
            fish.rect.y = random.randrange(alto)
            
            self.fish_lista.add(fish)
            self.lista_todos_los_sprites.add(fish)

        self.cat = Cat()
        self.lista_todos_los_sprites.add(self.cat)
        
        self.collect_sound = pygame.mixer.Sound('Drop_sound.mp3')
        
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.cat.changesspeed(-3, 0)
                if event.key == pygame.K_RIGHT:
                    self.cat.changesspeed(3, 0)
                if event.key == pygame.K_UP:
                    self.cat.changesspeed(0, -3)
                if event.key == pygame.K_DOWN:
                    self.cat.changesspeed(0, 3)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.cat.changesspeed(3, 0)
                if event.key == pygame.K_RIGHT:
                    self.cat.changesspeed(-3, 0)
                if event.key == pygame.K_UP:
                    self.cat.changesspeed(0, 3)
                if event.key == pygame.K_DOWN:
                    self.cat.changesspeed(0, -3)
                    
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    self.__init__()
                    
            
        return False
                
    def run_logic(self):
        
        if not self.game_over:
            self.lista_todos_los_sprites.update()
            
            self.fish_lista_completa = pygame.sprite.spritecollide(self.cat, self.fish_lista, True)
        
            for fish in self.fish_lista_completa:
                self.score += 1
                print(self.score)
                self.collect_sound.play()
                
            if len(self.fish_lista) == 0:
                self.game_over = True
        
        
    def display_frame(self, screen):
        screen.blit(background, [0, 0])
        
        if self.game_over:
            font = pygame.font.SysFont("Minecraft", 35)
            text = font.render("Game over - Press an arrow key to continue", False, white)
            center_x = (largo //  2) - (text.get_width() // 2)
            center_y = (alto // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            self.reset_game = True
            
        if not self.game_over:
            self.lista_todos_los_sprites.draw(screen)
        
        pygame.display.flip()

    
def main():
    pygame.init()
    
    size = (largo,  alto)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()
    
    pygame.mixer.music.load('Background_music.mp3')
    pygame.mixer.music.play(-1)
    
    game = Game()
    
    while not done:
        done = game. process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()



if __name__ == '__main__':
    main()