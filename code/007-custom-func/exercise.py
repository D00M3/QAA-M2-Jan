# Dice Roller 
import random

# Return a random number between 1 and 6
def rollSix():
    return random.randint(1,6)

def rollEight():
    return random.randint(1,8)

# Defaulting to size = 6 if no value is entered 
def rollDice(size=6):
    return random.randint(1, size)

def rollMultipleDice(number, size):
    diceValues = []
    # Loop as many times as number we pass in
    for x in range(number):
        diceValues.append(rollDice(size))
    
    dice_values = removeSmallest(diceValues)
    
    return diceValues

def removeSmallest(array_dice):
    print(array_dice)
    small = min(array_dice)
    array_dice.remove(small) # Removes the element of this value
    return array_dice

print(rollSix())
print(rollDice(12))
print(rollDice())
print(rollMultipleDice(4, 6))

# Taxes - Simple 
def simpleTax(salary):
    tax_percentage = 0

    if salary < 12570:
        tax_percentage = 0
    elif salary < 23000: 
        tax_percentage = 0.19
    elif salary < 40000:
        tax_percentage = 0.40
    else: 
        tax_percentage = 0.5
    
    taxable_amount = salary * tax_percentage
    return taxable_amount

