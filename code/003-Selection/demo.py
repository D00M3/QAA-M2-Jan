# Selection / Conditionals 
# If condition is true... do this thing, else... do thid thing

# = Assignment, set the value of this
colour = "purple"

# == Check, is this thing equal to this other thing 
if colour == "purple":
    print("Colour is purple :) ")
    print("any line that is indented is ran")
    print("runs when the if statement is true")
elif colour == "green":
    print("Colour is green")
elif colour == "red":
    print("Colour is red")
else:
    print("Unknown colour..")

print("This will always run")

chosen_num = int(input("Please enter a number between 1 and 100: "))

# Crocodile mouth goes towards the bigger thing
if chosen_num < 50: 
    print("number is less than 50")
elif chosen_num > 50: 
    print("Number is greater than 50")
else:
    print("number is 50")

test_boolean = True

if test_boolean == True:
    print("It is true!")
else:
    print("It is false..")

# Shorthand for test_boolean == true
if test_boolean:
    print("It is true!")
else: 
    print("it is false..")

test_false = False

if test_false == False:
    print("it is false")

if not test_false:
    print("It is false")