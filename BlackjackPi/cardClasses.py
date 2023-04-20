import random 


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return f"{self.val} of {self.suit}"



class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1,14):
                if j == 11:
                    j = "Jack"
                elif j == 12:
                    j = "Queen"
                elif j == 13:
                    j = "King"
                elif j == 1:
                    j = "Ace"
                self.cards.append(Card(i, j))

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    

class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        self.hand.append(deck.drawCard())
        return self
    

# deck = Deck()
# deck.shuffle()
# # print(deck.cards[0])

# player = Player()
# player.draw(deck)
# print(player.hand[0])
# print(player.hand[1])