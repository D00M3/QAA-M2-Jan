""" Module Doc String  """

from random import randint

DICE_NUMBER = 6

def rolllotsofdice():
    """ Function Doc String  """
    return randint(1,6)

print(rolllotsofdice())

def rolllotsofdice2():
    """ Function Doc String  """
    return randint(1,10)

def rollcustonnumbersss(numberone, numbertwo):
    """ Function Doc String  """
    return randint(numberone, numbertwo)

def checkrolls():
    """ Function Doc String  """
    if rolllotsofdice2() >= 6:
        return "big number!!!"
    return "small number :( "

CHECK_ROLLS = checkrolls()
print(CHECK_ROLLS)
LONG_VAR = "this is a really long variable that is integral"
