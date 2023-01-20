# Polymorphism
# Poly - multiple, or many
# Morph - Changing forms, or changing shapes
# Objects can take on multiple and many forms

# In python all objects are of type themselves and atleast the python super
# class object:
#     def __init__():
    
#     def _str__():
# if a class doesn't specify its parent, its parent is the python super object()
class animal:
    def sleep(self):
        return "*default zzz*"

class cat(animal):
    name = "zaph"
    # def sleep(self):
    #     return "*default purr*"

class lion(cat):
    food = "antelope"
    # def sleep(self):
    #     return "*roar and sleep*"

# animal is of type animal
animal = animal()
cat = cat() # cat is of type cat AND animal
lion = lion() # lion is of type, lion, cat and animal
print(animal.sleep())
print(cat.sleep())
print(cat.name)
print(lion.sleep())