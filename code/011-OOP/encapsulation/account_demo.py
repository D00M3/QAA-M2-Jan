# Python has no concept of private variables
# No way of hiding and securing variables so modules and code can't change 

# Encapsulation - Only trusted code should have 
# limited access to functionality and variables
# - Grouping together all functions and methods of getting and setting data

# Leading underscore suggests to devs that this is a private variable
class bankAccount:
    
    _pin = "1234"
    _money = 500

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # getter
    def displayMoney(self, pin):
        if pin == self._pin:
            return self._money
        else:
            return "Invalid Pin!"

    # Setter
    def depositMoney(self, pin, money):
        if pin == self._pin:
            self._money += money
            return f"Total money: {self._money}"
        else:
            return "Invalid pin!"

    # Setter
    def setAge(self, age):
        if age < self.age:
            return "Invalid age choice.."
        else:
            self.age = age


acc1 = bankAccount("Reece", 27)
print(acc1._pin) # 1234, not secure!
print(acc1.displayMoney("1234"))
print(acc1._money)
print(acc1.depositMoney("5555", 456))
# print(acc1.getMoney())

