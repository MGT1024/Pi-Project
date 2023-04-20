from functools import reduce
from basicStrategyDict import *
import random
# hands 
dealerUpCard = []
hand = []
points = 0
card1, val1 = random.choice(list(deckOfCards.items()))
card2, val2 = random.choice(list(deckOfCards.items()))
hand.append(card1)
hand.append(card2)
points += (val1+val2)
print(f"Hand: {hand}, Points: {points}")


dealers, val= random.choice(list(deckOfCards.items()))
dealerUpCard.append(dealers)
print(f"Dealer's showing a {dealers}, {val} points")







# if hand[0] == 11:
#     print(softTotalDict[hand[0]][dealerUpCard])

# elif hand[0] == hand[1]:
#     print(pairSplittingDict[hand[0]][dealerUpCard])

# else:
#     print(hardTotalDict[handTotal][dealerUpCard])


# def hardTotal():
#     hardTotalDict[None][None]

# def softTotal():
#     softTotalDict[None][None]

# def pairSplitting():
#     pairSplittingDict[None][None]


