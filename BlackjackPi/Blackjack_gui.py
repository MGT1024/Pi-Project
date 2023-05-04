import pygame
import Cards 
from sys import exit
from interactFile import *
from word2number import w2n
clearData()
full_card_list = []

##TODO##

# FUNCTIONS #
def start():
    for i in range(len(loadData())):
        if i % 2 == 0:
            PLAYER.take_card()
        else:
            DEALER.take_card()

def display_text():
    dealer_text_surf = text_font.render(f"Dealer Hand: {DEALER.card_vals}", False, "limegreen")
    dealer_text_rect = dealer_text_surf.get_rect(topleft = (10, 100))
    screen.blit(dealer_text_surf, dealer_text_rect)

    player_text_surf = text_font.render(f"Player Hand: {PLAYER.card_vals}", False, "limegreen")
    player_text_rect = player_text_surf.get_rect(topleft = (10, 225))
    screen.blit(player_text_surf, player_text_rect)

# CLASSES #
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hand_xcoord = 10
        self.hand_ycoord = 250
        self.hand = pygame.sprite.Group()
        self.card_vals = 0
        self.number_aces = 0
        self.status = "Playing"
        self.turn = True
    
    def take_card(self):
        DECK.addCard(self.hand_xcoord, self.hand_ycoord)
        current_card = Card(DECK.drawCard(), self.hand_xcoord, self.hand_ycoord, False)
        if current_card.face == "ace": self.number_aces += 1
        self.card_vals += current_card.val
        self.calc_score()
        self.hand.add(current_card)
        self.hand_xcoord += 50

    def clear_hand(self):
        self.hand_xcoord = 10
        self.hand.empty()
        self.card_vals = 0

    def display_status(self):
        status_surf = text_font.render(f"Status: {self.status}", False, "limegreen")
        status_rect = status_surf.get_rect(topleft = (10, 0))
        screen.blit(status_surf, status_rect)
    
    def calc_score(self):
        total = self.card_vals
        aces = self.number_aces
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        self.card_vals = total
        self.number_aces = aces
        if self.card_vals > 21:
            self.turn = False
            self.lose()

    def lose(self):
        self.status = "Lost"

    def win(self):
        self.status = "Won"
    
    def tie(self):
        self.status = "Push"

    def update(self):
        self.display_status()

class Dealer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hand_xcoord = 10
        self.hand_ycoord = 125
        self.hand = pygame.sprite.Group()
        self.hidden_card = pygame.sprite.GroupSingle()
        self.card_vals = 0
        self.turn = False
        self.number_aces = 0

    def take_card(self):
        DECK.addCard(self.hand_xcoord, self.hand_ycoord)
        current_card = Card(DECK.drawCard(), self.hand_xcoord, self.hand_ycoord, False)
        if current_card.face == "ace": self.number_aces += 1
        self.card_vals += current_card.val
        self.calc_score()
        self.hand.add(current_card)
        self.hand_xcoord += 50
    
    def add_dummy_card(self):
        self.hidden_card.add(Card("hidden0", 60, self.hand_ycoord, True))

    def clear_hand(self):
        self.hand_xcoord = 10
        self.card_vals = 0
        self.hand.empty()
    
    def calc_score(self):
        global game_active
        total = self.card_vals
        aces = self.number_aces
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        self.card_vals = total
        self.number_aces = aces
        if self.card_vals >= 17: 
            self.win_or_loss()
            game_active = False

    def win_or_loss(self):
        if self.card_vals < PLAYER.card_vals and PLAYER.card_vals <= 21: 
            PLAYER.win()
        elif self.card_vals > PLAYER.card_vals and self.card_vals <= 21: 
            PLAYER.lose()
        elif self.card_vals > 21 and PLAYER.card_vals <= 21:
            PLAYER.win()
        # elif PLAYER.card_vals > 21 and self.card_vals <= 21:
        #     PLAYER.lose()
        else:
            PLAYER.tie()
        DEALER.turn = False
        PLAYER.turn = False

    def update(self):
        pass

class StandButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("BlackjackPi\\images\\stand button.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect =  self.image.get_rect(midbottom = (700, 275))     
 
class HitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BlackjackPi\\images\\hit button.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.rect =  self.image.get_rect(midbottom = (700, 150))

class Card(pygame.sprite.Sprite):
    def __init__(self, card_info, x_coord, y_coord, hidden=False):
        super().__init__()
        self.suit = card_info[-1]
        self.face = card_info[:-1]
        self.val = 0
        self.hidden = hidden
        if self.face == "ace":
            self.val = 11
        elif self.face == "jack":
            self.val = 10
        elif self.face == "queen":
            self.val = 10
        elif self.face == "king":
            self.val = 10
        elif self.face == "hidden":
            self.val = 0
        else:
            self.val = w2n.word_to_num(self.face)
        
        if self.val > 11:
            self.val = 10

        if self.hidden == True: self.image = pygame.image.load("BlackjackPi\\images\\cards\\cardback.png") 
        else: self.image = pygame.image.load(f"BlackjackPi\\images\\cards\\card{self.face}{self.suit}.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(topleft = (x_coord, y_coord))

class Deck:
    def __init__(self):
        self.deck = pygame.sprite.Group()
    
    def addCard(self, x_pos, y_pos, hidden=False):
        global full_card_list, card_index
        if len(full_card_list) < len(loadData()):
            for i in range(len(loadData())):
                if loadData()[i] not in full_card_list:
                    full_card_list.append(loadData()[i])
        card_index += 1
        return Card(full_card_list[card_index-1], x_pos, y_pos, hidden)

    def drawCard(self):
        return full_card_list[card_index-1]

# MAIN #
pygame.init()

# defines the ratio of the screen
screen = pygame.display.set_mode((800, 400))

# sets the title of the window
pygame.display.set_caption('Black Jack')

# clock for fps
clock = pygame.time.Clock()

# game state
game_active = False

# font
text_font = pygame.font.Font("BlackjackPi\\font\\LGGothic.ttf", 25)

# background
bg_img = pygame.image.load("BlackjackPi\\images\\blackjack background.png").convert_alpha()

# buttons
hit_button = pygame.sprite.GroupSingle()
hit_button.add(HitButton())

stand_button = pygame.sprite.GroupSingle()
stand_button.add(StandButton())

# deck
DECK = Deck()
# DECK.shuffle()

# dealer
DEALER = Dealer()

# player
PLAYER = Player()

# setting rate that dealer deals cards
deal_event = pygame.USEREVENT + 1
pygame.time.set_timer(deal_event, 1000)

card_index = 0

current_cards = len(loadData())

DEALER.add_dummy_card()

# LOOP #
while True:
    # tests for every button press in each frame
    for event in pygame.event.get():
        
        # if the window is closed
        # the program ends seamlessly
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
        mouse_pos = pygame.mouse.get_pos()
        # implement gpio button features
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hit_button.sprite.rect.collidepoint(mouse_pos):
                clearData()
                Cards.clear_list()
                card_index = 0
                full_card_list = []
                PLAYER.clear_hand()
                PLAYER.status = "Playing"
                DEALER.clear_hand()
                DEALER.hidden_card.empty()
                game_active = False
            if game_active and PLAYER.turn:
                
                if stand_button.sprite.rect.collidepoint(mouse_pos):
                    PLAYER.turn = False
                    DEALER.turn = True

    if game_active:
        if current_cards != len(loadData()) and len(loadData()) != 3:
            if PLAYER.turn:
                PLAYER.take_card() 
                current_cards = len(loadData())
            elif DEALER.turn:
                DEALER.take_card()
                current_cards = len(loadData())

    else:
        if len(loadData()) == 3:
            start()
            current_cards = len(loadData())
            game_active = True
            PLAYER.turn = True
            DEALER.turn = False
            DEALER.add_dummy_card()
        
    screen.blit(bg_img, (0, 0))
    
    stand_button.draw(screen)
    
    hit_button.draw(screen)
    
    display_text()
    
    PLAYER.update()
    PLAYER.hand.draw(screen)

    if not PLAYER.turn and DEALER.turn: DEALER.update()

    if game_active: DEALER.hidden_card.draw(screen)

    DEALER.hand.draw(screen)


    # updates window
    pygame.display.update()
    # caps at 60 fps
    clock.tick(60)