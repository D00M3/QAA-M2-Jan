# function
# Creating our function 
def greeting():
    print("Hello!")

def greetingReturn():
    print("Print message")
    return "return message" # Return is what this function is equal to 

# Calling our function 
greeting()
print(greeting())
print(greetingReturn())

# colour can be ANYTHING, number, boolean, string, array, function etc.
def colourFunc(colour):
    return f"Colour is {colour}"

# Call back function, passing in a function as a param
colourFunc("green") # same as just typing "colour is Green"
print(colourFunc("green"))

def greetCallBack(function):
    return f"Hello {function}, how are you?"
    print("this is text")

def nameFunc(name):
    return name.title()

greeting = greetCallBack(nameFunc("reece"))

# Scope - What functions and processes have access to variables

global_var = "NOT SECRET"

def sum(x, y):
    print(global_var)
    total = x + y
    private_var = "SECRET" # Only accessible inside of this variable
    return total # Returning a variable outputs it to the scope

# print(private_var)
print(sum(5, 10)) # equal to total