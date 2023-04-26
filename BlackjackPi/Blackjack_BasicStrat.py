from functools import reduce
from basicStrategyDict import *
import random
from gpio import *
from time import sleep
# from gpio import *
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

if val == "A":
    val = 11



if (val1 == 11 or val2 == 11) and (val1 == 10 or val2 == 10):
    print("Blackjack!")
    quit()
    

#   HARD TOTALS
def outputs():
    if "A" not in hand and val1 != val2:
        output = (hardTotalDict[points][val])
        print(output)


    if "A" == hand[0] and hand[0] != hand[1]:
        output = (softTotalDict[val2][val])
        print(output)

    if "A" == hand[1] and hand[0] != hand[1]:
        output = (softTotalDict[val1][val])
        print(output)

    if val1 == val2:
        output = (pairSplittingDict[val1][val])
        print(output)

    match output: 
        case "HIT":
            HIT = True
            sleep(1)
            HIT = False
        case "STAND":
            STAND = True
            sleep(1)
            STAND = False
        case "SPLIT":
            SPLIT = True
            sleep(1)
            SPLIT = False
        case "DOUBLE DOWN":
            DOUBLE = True
            sleep(1)
            DOUBLE = False
