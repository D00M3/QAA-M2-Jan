class lizard:

    _lizard_password = "eggplant"

    def __init__(self, colour, legs, tail):
        self._colour = colour
        self._legs = legs
        self._tail = tail

    def breathe(self):
        return "*gentle lizard breathing*"

    def __str__(self):
        return "This is what is printed when you print(lizard1)"

    # getters - Used to get data from an object
    def getColour(self):
        return self._colour

    def getLegs(self, password):
        if password == self._lizard_password:
            return self._legs
        else:
            return "wrong password!"

    # Setters - Used to set the data within an object

    def setLegs(self, number):
        if number > 4:
            self._legs = number
            return True
        else:
            return "Incorrect number of legs.. "

lizard1 = lizard("green", 3, False)
# lizard1.legs = "has legs" # bad practice because legs should be an int
print(lizard1.setLegs(7))