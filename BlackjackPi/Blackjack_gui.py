import pygame
from sys import exit
from random import randint, choices
##TODO##
# Add dealer and player logic to hit and stand

# FUNCTIONS #
def display_money(money):

    money_surf = text_font.render(f'Money: {money}', False, (255, 255, 255))
    money_rect = money_surf.get_rect(topleft = (10, 0))
    screen.blit(money_surf, money_rect)

# CLASSES #
class StandButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("BlackjackPi\\images\\stand button.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect =  self.image.get_rect(midbottom = (700, 275))

    def stand(self):
        pass
        
class HitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BlackjackPi\\images\\hit button.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect =  self.image.get_rect(midbottom = (700, 150))
    
    def hit(self):
        pass

class Card():
    pass

class Cheater():
    pass

# VARS #
game_active = True

money_amount = 0
# MAIN #
pygame.init()
# defines the ratio of the screen
screen = pygame.display.set_mode((800, 400))
# sets the title of the window
pygame.display.set_caption('Black Jack')
# clock for fps
clock = pygame.time.Clock()

text_font = pygame.font.Font("BlackjackPi\\font\\LGGothic.ttf", 25)

bg_img = pygame.image.load("BlackjackPi\\images\\blackjack background.png").convert_alpha()

hit_button = pygame.sprite.GroupSingle()
hit_button.add(HitButton())

stand_button = pygame.sprite.GroupSingle()
stand_button.add(StandButton())

dealer_cards = pygame.sprite.Group()

player_cards = pygame.sprite.Group()

# LOOP #
while True:
    # tests for every button press in each frame
    for event in pygame.event.get():
        
        # if the window is closed
        # the program ends seamlessly
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stand_button.sprite.rect.collidepoint(mouse_pos):
                    pass
                if hit_button.sprite.rect.collidepoint(mouse_pos):
                    pass

    if game_active:
        screen.blit(bg_img, (0, 0))

        stand_button.draw(screen)

        hit_button.draw(screen)

        money = display_money(money_amount)



    # updates window
    pygame.display.update()
    # caps at 60 fps
    clock.tick(60)