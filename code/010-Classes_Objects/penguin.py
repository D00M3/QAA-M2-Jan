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
        return "Swimming quickly!"

penguin1 = penguin("pingu", 15, True)
penguin2 = penguin("paulie", 0, False)
print(penguin1.dancing)

# Convert / make new classes using proper constructors to set values 
# Make 2 objects with different values 