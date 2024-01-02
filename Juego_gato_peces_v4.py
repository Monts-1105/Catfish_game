import pygame, random

largo = 800
alto = 600
white = (255, 255, 255)
black = (0, 0, 0)

secs = 30

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
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.cat.changesspeed(-3)
                if event.key == pygame.K_RIGHT:
                    self.cat.changesspeed(3)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.cat.changesspeed(0)
                if event.key == pygame.K_RIGHT:
                    self.cat.changesspeed(0)
                    
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    self.game_over = False
                    self.initialized = False
                    self.__init__()
                    
            
        return False
                
    def run_logic(self):
        
        if not self.game_over:
            
            current_time = pygame.time.get_ticks()
            remaining_time = max(0, (self.timer - current_time) // 1000)
            print("Time:", remaining_time)
            
            self.lista_todos_los_sprites.update()
            
            self.fish_lista_completa = pygame.sprite.spritecollide(self.cat, self.fish_lista, True)
        
            for dead_fish in self.fish_lista_completa:
                self.score -= 3
                print(self.score)
                self.collect_sound.play()
                
            for blue_fish in self.fish_lista_completa:
                self.score += 3
                print(self.score)
                self.collect_sound.play()
                
            for gold_fish in self.fish_lista_completa:
                self.score += 5
                print(self.score)
                self.collect_sound.play()
            
            print("Score", self.score)
                
            if remaining_time == 0:
                self.game_over = True
                
                self.fish_lista.empty()
                self.lista_todos_los_sprites.empty()
                
                if not self.initialized:
                    self.initialized = True
                    self.__init__()
        
        
    def display_frame(self, screen):
        screen.blit(background, [0, 0])
        font = pygame.font.Font(None, 30)
        text = font.render('Time: {}'.format(max(0, (self.timer - pygame.time.get_ticks()))), True, white)
        screen.blit(text, (10, 10))
        score_font = pygame.font.Font(None, 30)
        score_text = score_font.render('Score: {}'.format(self.score), False, white)
        screen.blit(score_text, (700, 10))
        
        if self.game_over:
            font = pygame.font.SysFont("Arial", 35)
            text = font.render("Game over - Press an arrow key to continue", False, white)
            center_x = (largo //  2) - (text.get_width() // 2)
            center_y = (alto // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            
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