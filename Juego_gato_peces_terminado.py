import pygame, random

largo = 800
alto = 600
white = (255, 255, 255)
black = (0, 0, 0)

secs = 25

background = pygame.image.load('lake.jpg')
background =  pygame.transform.scale(background, (900, 600))

class Dead_fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dead_fish.png').convert()
        self.image.set_colorkey(white)
        self.image =  pygame.transform.scale(self.image, (60, 45))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 2
        
        if self.rect.y > alto:
            self.rect.y = -10
            self.rect.x = random.randrange(largo)
            
class Blue_fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('blue_fish.png').convert()
        self.image.set_colorkey(black)
        self.image =  pygame.transform.scale(self.image, (60, 45))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 3
        
        if self.rect.y > alto:
            self.rect.y = -10
            self.rect.x = random.randrange(largo)
            
class Gold_fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('gold_fish.png').convert()
        self.image.set_colorkey(white)
        self.image =  pygame.transform.scale(self.image, (60, 45))
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += 5
        
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
        
    def changesspeed(self, x):
        self.vel_x += x
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y = 270


class Game(object):
    def __init__(self):
        self.game_over = False
        self.timer = pygame.time.get_ticks() + secs * 1000
        
        self.score = 0
        
        self.fish_lista = pygame.sprite.Group()
        self.lista_todos_los_sprites = pygame.sprite.Group()
        
        for i in range(10):
            dead_fish = Dead_fish()
            dead_fish.rect.x = random.randrange(largo)
            dead_fish.rect.y = random.randrange(alto)
            
            self.fish_lista.add(dead_fish)
            self.lista_todos_los_sprites.add(dead_fish)
        
        self.collect_sound = pygame.mixer.Sound('Pick_sound.mp3')
        
        
        for i in range(30):
            blue_fish = Blue_fish()
            blue_fish.rect.x = random.randrange(largo)
            blue_fish.rect.y = random.randrange(alto)
            
            self.fish_lista.add(blue_fish)
            self.lista_todos_los_sprites.add(blue_fish)
        
        self.collect_sound = pygame.mixer.Sound('Pick_sound.mp3')
        
        
        for i in range(15):
            gold_fish = Gold_fish()
            gold_fish.rect.x = random.randrange(largo)
            gold_fish.rect.y = random.randrange(alto)
            
            self.fish_lista.add(gold_fish)
            self.lista_todos_los_sprites.add(gold_fish)

        self.cat = Cat()
        self.lista_todos_los_sprites.add(self.cat)
        
        self.collect_sound = pygame.mixer.Sound('Pick_sound.mp3')
        self.initialized = False
        self.arrow_key_pressed = False
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_LEFT]:
            self.cat.changesspeed(-0.5)
        elif keys[pygame.K_RIGHT]:
            self.cat.changesspeed(0.5)
    
        if self.game_over:
            if self.game_over and any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]):
                if not self.arrow_key_pressed:
                    self.arrow_key_pressed = True
                    self.game_over = False
                    self.initialized = False
                    self.__init__()
            else:
                self.arrow_key_pressed = False

            
        return False
                
    def run_logic(self):
        
        if not self.game_over:
            
            current_time = pygame.time.get_ticks()
            remaining_time = max(0, (self.timer - current_time) // 1000)
            print("Time:", remaining_time)
    
            self.lista_todos_los_sprites.update()
    
            self.fish_lista_completa = pygame.sprite.spritecollide(self.cat, self.fish_lista, True)
    
            for fish in self.fish_lista_completa:
                if isinstance(fish, Dead_fish):
                    self.score -= 3
                    self.collect_sound.play()
                elif isinstance(fish, Blue_fish):
                    self.score += 3
                    self.collect_sound.play()
                elif isinstance(fish, Gold_fish):
                    self.score += 5
                    self.collect_sound.play()
    
            print("Score", self.score)
    
            for fish in self.fish_lista_completa:
                fish.kill()
    
            if remaining_time == 0:
                self.game_over = True
    
        # Lógica de reinicio del juego
        if self.game_over and pygame.key.get_pressed()[pygame.K_LEFT]:
            self.game_over = False
            self.initialized = False
            self.__init__()
        
        
    def display_frame(self, screen):
        screen.blit(background, [0, 0])
        font = pygame.font.Font(None, 30)
        

        
        if self.game_over:
            font = pygame.font.SysFont("Arial", 30)
            text = font.render("Game over - Presiona una tecla de flecha para volver a empezar", False, white)
            center_x = (largo //  2) - (text.get_width() // 2)
            center_y = (alto // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            
        if not self.game_over:
            text = font.render('Time: {}'.format(max(0, (self.timer - pygame.time.get_ticks()))), True, white)
            screen.blit(text, (10, 10))
            score_font = pygame.font.Font(None, 30)
            score_text = score_font.render('Score: {}'.format(self.score), False, white)
            screen.blit(score_text, (700, 10))
            score_text = score_font.render('Blue fish x3', False, white)
            screen.blit(score_text, (10, 30))
            score_text = score_font.render('Gold fish x5', False, white)
            screen.blit(score_text, (10, 50))
            score_text = score_font.render('Dead fish x -3', False, white)
            screen.blit(score_text, (10, 70))
            text = font.render("Recolecta la mayor cantidad de pescados vivos sin recolectar los muertos", False, white)
            screen.blit(text, (30, 580))
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