from abc import ABC, abstractmethod

# Abstraction - Abstract, non physical conceptual model 
# Classes and objects, objects are 'physical'
# Abstract classes, which are classes we cannot create objects from 

# Abstract class is more of a plan / concept of a different class 

# Abstract classes - they are used to plan regular classes
# import ABC from the abc package, ABC - Abstract Base Class 

class animal(ABC):
    # There's no need to have a constructor.. as we can't create an animal

    # We are defining an empty function that has no body (functionality)
    # Declaring a variable before starting code
    @abstractmethod 
    def breathe(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Regular class
class lizard(animal):

    def __init__(self, colour, legs, tail):
        self.colour = colour
        self.legs = legs
        self.tail = tail

    def breathe(self):
        return "*gentle lizard breathing*"

    def __str__(self):
        return "This is what is printed when you print(lizard1)"
    
lizard1 = lizard("beige, golden", 4, True)
print(lizard1.legs)
print(lizard1)
# animalObj = animal()
# print(animalObj)