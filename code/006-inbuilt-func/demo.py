# numbers = [19, 45, 32, 7, -21, 10, -42, 1.23, 56.9831]

# print(numbers)

# # min (and other numerical functions) only work with nums
# print(min(numbers))
# print(max(numbers))
# # Converts negative to positive
# print(abs(numbers[4]))
# # To the power of 2 * 2 * 2, works the same as 2**3
# print(pow(2,3))
# # round numbers to decimal points
# print(round(numbers[-1])) 
# print(round(numbers[-1], 2)) 

# Strings are complex data types, made up of simpler data types
# They contain inbuilt functions as they are complex 
# String formatting 
str = "hElLo WoRlD"
print(str.lower())
print(str.upper())
print(str.title()) # Hello World
print(str.lower().replace("l", "z")) # Replaces all l's with z's
print(str.center(10, '='))

cities = "london,cardiff,newport,glasgow,leeds"
citylist = cities.split(",")
print(citylist)

for city in citylist:
    print(city)

# String formatting 
drink = "mocha"
size = "large"
extras = "whipped cream"
order = "{} ordered at size {} with {} added".format(drink, size, extras)
print(order)