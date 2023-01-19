class penguin: 

    # You specify attributes and what data type they are
    # Constructor, function that takes in params and sets the attributes
    # of our created object
    # __init__ - the initialising function that runs when the object starts
    def __init__(self, name, fish_eaten, dancing):
        self.name = name
        self.fish_eaten = fish_eaten
        self.dancing = dancing 
        # Setting the values of our object based on whats entered
    
    def swim(self):
        return f"{self.fish_eaten} fish.. swimming to get more fish!"

    # What is returned when we print off an object
    def __str__(self):
        return f"name: {self.name}   fish eaten: {self.fish_eaten}   dancing: {self.dancing}"


penguin1 = penguin("pingu", 15, True)
penguin2 = penguin("paulie", 0, False)
print(penguin1.dancing)

print(penguin1.name)
print(penguin1.swim())

# Convert / make new classes using proper constructors to set values 
# Make 2 objects with different values 
# Stretch goal - make your function refer to and use an attribute
print("===========================================")
print(penguin1)
print(penguin2)

print(dir(penguin1)) # Prints off all attributes of an object


# Other useful functions 
# getattr() - Gets the value of a specific attr from an object
print(getattr(penguin1, 'name'))
# hasattr() - Returns true or false if it contains this attribute
print(hasattr(penguin2, 'flight_speed'))
# setattr() - set the value of an atteribute (create new attributes)
setattr(penguin2, 'flight_speed', 34)
print(hasattr(penguin2, 'flight_speed'))

print(penguin2.flight_speed)
# delattr() - Deletes an attribute of this name
delattr(penguin2, 'flight_speed')

# Exercise - Modify your to string __str__ and use 
# hasattr, getattr, setattr, delattr to change object