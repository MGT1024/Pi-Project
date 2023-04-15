from functools import reduce
from basicStrategyDict import *
import random
# hands 
hand = []
for i in deckOfCards:
    hand = hand + deckOfCards[i]
    for y in deckOfCards:
        hand = hand +deckOfCards[y]
        print(hand)

dealers = random.choice(deckOfCards.keys)
print (dealers)
dealerUpCard = None
handTotal = reduce(lambda x, y: x+y, hand)



if hand[0] == 11:
    print(softTotalDict[hand[0]][dealerUpCard])

elif hand[0] == hand[1]:
    print(pairSplittingDict[hand[0]][dealerUpCard])

else:
    print(hardTotalDict[handTotal][dealerUpCard])


def hardTotal():
    hardTotalDict[None][None]

def softTotal():
    softTotalDict[None][None]

def pairSplitting():
    pairSplittingDict[None][None]


Running = True

while Running:
    pass