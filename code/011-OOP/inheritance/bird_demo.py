class bird:

    def __init__(self, feather_colour, wingspan, type):
        self.feather_colour = feather_colour
        self.wingspan = wingspan
        self.type = type

    def noise(self):
        return "*default bird noise*"

# When making a child class we specify the parent using ()
class penguin(bird):
    def __init__(self, feather_colour, wingspan, type, swim_speed):
        super().__init__(feather_colour, wingspan, type) # Run the parent class __init__ function
        self.swim_speed = swim_speed

    # Overriding the noise() function for penguins
    def noise(self):
        return "GAK GAK GAK"

penguin1 = penguin("black and white", 32, "cold water bird", 50)
print(penguin1.feather_colour)
print(penguin1.noise())

class eagle(bird):
    def __init__(self, feather_colour, wingspan, type, fly_speed):
        super().__init__(feather_colour, wingspan, type)
        self.fly_speed = fly_speed

eagle1 = eagle("grey", 98, "big freedom bird", 140)

# Exercise - Create a parent class that has 2+ children passing down 3x attributes and 1 function
# Child class should contain a __str__ which prints all attributes of this object
# Create 1x object of each child class 