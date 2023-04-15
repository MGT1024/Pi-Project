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
                self.cards.append(Card(i, j))

    def show(self):
        for cards in self.cards:
            cards.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
deck = Deck
deck.show()



card = Card("Card", 6)
card.show()
