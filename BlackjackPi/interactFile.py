DATAFILE = "data.txt"

def saveData(cardList):
    # print(cardList)
    with open(DATAFILE, "w") as file:
        for card in cardList:
            file.write(card + ",")
        file.close()

def loadData():
    data = []
    with open(DATAFILE, "r") as file:
        data = file.readline().split(",")[:-1]
        # print(data)
    return data

def clearData():
    with open(DATAFILE, "w") as file:
        file.write("")
        file.close()