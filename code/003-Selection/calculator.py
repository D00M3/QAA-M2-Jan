# print(
#     """
#     You can enter 
#     multiple lines
#     of code at once
#     and its pretty useful
#     """
# )

print(
    """
    Welcome to the calculator app!
    Please choose a command 
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Power
    """
)

sum = input("Please enter number of chosen sum: ")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

if sum == "1":
    print(f"{num1} + {num2} = {num1 + num2}")
elif sum == "2":
    print(f"{num1} - {num2} = {num1 - num2}")
elif sum == "5":
    print(f"{num1} to the power of {num2} is {num1**num2}")