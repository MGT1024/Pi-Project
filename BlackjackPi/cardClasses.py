import random



class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val


    def show(self):
        print(f"{self.value} of {self.suit}")


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



    def show(self):
        for cards in self.cards:
            cards.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()
# deck.show()

gunt = Player("Gunt")
gunt.draw(deck)
gunt.showHand()


# card = Card("Card", 6)
# card.show()
