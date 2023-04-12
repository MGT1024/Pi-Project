deckOfCards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}
hardTotalDict = {
    20: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND",
    },
    19: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND",
    },
    18: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND",
    },
    17: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND",
    },
    16: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    15: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    14: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    13: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    12: {
    2: "HIT",
    3: "HIT",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    11: {
    2: "DOUBLE DOWN",
    3: "DOUBLE DOWN",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "DOUBLE DOWN",
    8: "DOUBLE DOWN",
    9: "DOUBLE DOWN",
    10: "DOUBLE DOWN",
    "A": "DOUBLE DOWN",
    },
    10: {
    2: "DOUBLE DOWN",
    3: "DOUBLE DOWN",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "DOUBLE DOWN",
    8: "DOUBLE DOWN",
    9: "DOUBLE DOWN",
    10: "HIT",
    "A": "HIT",
    },
    9: {
    2: "HIT",
    3: "DOUBLE DOWN",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    8: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "HIT",
    6: "HIT",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    7: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "HIT",
    6: "HIT",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    6: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "HIT",
    6: "HIT",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    5: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "HIT",
    6: "HIT",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
    4: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "HIT",
    6: "HIT",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT",
    },
}
softTotalDict = {
    9: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND"
    },
    8: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "DOUBLE DOWN",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND"
    },
    7: {
    2: "DOUBLE DOWN",
    3: "DOUBLE DOWN",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "STAND",
    8: "STAND",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    },
    6: {
    2: "HIT",
    3: "DOUBLE DOWN",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    },
    5: {
    2: "HIT",
    3: "HIT",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    },
    4: {
    2: "HIT",
    3: "HIT",
    4: "DOUBLE DOWN",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    },
    3: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    },
    2: {
    2: "HIT",
    3: "HIT",
    4: "HIT",
    5: "DOUBLE DOWN",
    6: "DOUBLE DOWN",
    7: "HIT",
    8: "HIT",
    9: "HIT",
    10: "HIT",
    "A": "HIT"
    }
}
pairSplittingDict = {
    "A": {
    2: "SPLIT",
    3: "SPLIT",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "SPLIT",
    8: "SPLIT",
    9: "SPLIT",
    10: "SPLIT",
    "A": "SPLIT"
    },
    10: {
    2: "STAND",
    3: "STAND",
    4: "STAND",
    5: "STAND",
    6: "STAND",
    7: "STAND",
    8: "STAND",
    9: "STAND",
    10: "STAND",
    "A": "STAND"
    },
    9: {
    2: "SPLIT",
    3: "SPLIT",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "STAND",
    8: "SPLIT",
    9: "SPLIT",
    10: "STAND",
    "A": "STAND"
    },
    8: {
    2: "SPLIT",
    3: "SPLIT",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "SPLIT",
    8: "SPLIT",
    9: "SPLIT",
    10: "SPLIT",
    "A": "SPLIT"
    },
    7: {
    2: "SPLIT",
    3: "SPLIT",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    },
    6: {
    2: "SPLIT AND DOUBLE DOWN",
    3: "SPLIT",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "DO NOT SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    },
    5: {
    2: "DO NOT SPLIT",
    3: "DO NOT SPLIT",
    4: "DO NOT SPLIT",
    5: "DO NOT SPLIT",
    6: "DO NOT SPLIT",
    7: "DO NOT SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    },
    4: {
    2: "DO NOT SPLIT",
    3: "DO NOT SPLIT",
    4: "DO NOT SPLIT",
    5: "SPLIT AND DOUBLE DOWN",
    6: "SPLIT AND DOUBLE DOWN",
    7: "DO NOT SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    },
    3: {
    2: "SPLIT AND DOUBLE DOWN",
    3: "SPLIT AND DOUBLE DOWN",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    },
    2: {
    2: "SPLIT AND DOUBLE DOWN",
    3: "SPLIT AND DOUBLE DOWN",
    4: "SPLIT",
    5: "SPLIT",
    6: "SPLIT",
    7: "SPLIT",
    8: "DO NOT SPLIT",
    9: "DO NOT SPLIT",
    10: "DO NOT SPLIT",
    "A": "DO NOT SPLIT"
    }
}
