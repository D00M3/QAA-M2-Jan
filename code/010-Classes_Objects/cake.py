# Class for Cake
# Class - Recipe, blueprint for what we want our objects to be

# Class has a default function called a 
# constructor that we can use to make objects
class cake:
    frosting = True
    flavour = "choc"
    size = 15

    def bake(self):
        return "In the oven now!"

cake1 = cake()
print(cake1) # <__main__.cake object at 0x00000227D494E9D0>
print(cake1.frosting) # Object Frosting - true
print(cake.frosting) # Class frosting - True

print(cake1.bake())

# Exercise - Create a class and 2x objects 
# of your animal working on in SQL