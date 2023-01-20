class calculator:

    # Scientific calculator or not
    # Rounds up or down
    # Specific functions to use
    # What colour is the calculator
    def __init__(self, scientific, colour, brand):
        self.scientific = scientific
        self.colour = colour
        self.brand = brand

    def add(self, x, y):
        if self.scientific:
            return f"{x} + {y} = 1x10^{x + y}"
        else:
            return f"{x} + {y} = {x + y}"

    def sub(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y


calc1 = calculator(True, "Dark Blue", "Casio")
calc2 = calculator(False, "Orange and yellow", "Nerf")

print(calc1.add(5,7))
print(calc2.add(5,7))