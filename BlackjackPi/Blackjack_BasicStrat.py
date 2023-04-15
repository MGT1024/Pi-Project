from functools import reduce
from basicStrategyDict import deckOfCards, hardTotalDict, softTotalDict, pairSplittingDict

# hands penis
hand = [deckOfCards[None], deckOfCards[None]]
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