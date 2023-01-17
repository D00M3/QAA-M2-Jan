import random

def rollDice(size, number):
    total = 0
    diceValues = []
    for x in range(number):
        value = random.randint(1, size)
        diceValues.append(value)
    
    return diceValues

print(rollDice(8,2))
