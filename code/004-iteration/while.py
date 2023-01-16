# Importing in the random package
import random 

# Iteration - Repeating a block of code to save time and development

# While Loop 
# While loop runs a block of code until a condition is no longer true
counter = 1
while counter <= 100: 
    print(f"Value of counter is {counter}")
    # assigning counter to a new value which is old value + 1
    # counter = counter + 1
    counter += random.randint(2, 15) 

    if counter == 50: 
        print("Hit value 50 exactly!")
        break # Stops the loop from running
    # 10 min break, back for 14:45