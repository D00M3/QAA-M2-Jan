# Arrays are the umbrella term for collections of data
# Lists - [] ordered, mutable
# tuples - () ordered, immutable
# dictionaries - {} unordered, mutable, key value
# Sets - {} unordered, mutable, unique

animals = ["aardvark", "sloth", "aiai", "zebra"]
print(animals[2])
print(animals[-2])
animals[1] = "panda"
print(animals[1])
print("panda" in animals)
print("sloth" in animals)
animals.append("tiger")
print(animals)

# Insert takes in an index position, and a value 
animals.insert(2, "tardegrade")
print(animals)

# Lists can take in any data type
cafe_order = [12, "John Cena", True, ["latte", "carrot cake"]]
print(cafe_order[3][1])

# Length of a list (how many elements)
print(len(animals))

print("====================================")
print(*animals, sep="\n")

for somethingRandom in animals:
    print(somethingRandom)


# Tuples - Cannot be modified
colours = ("red", "green", "blue", "purple")
print(colours[2])
# colours[2] = "gold" You can't change values

# Just recreate the tuple
colours = ("silver")
print(colours)

# Dictionaries - Unordered, mutable, key: value pairs
noises = {"cow": "moo!", "duck": "quack!"}
print(noises["cow"]) 
noises["chicken"] = "cluck!"
print(noises)

noises["number"] = 123
print(noises)

# Sets - Unordered, unique values 
fruit = {"lemon", "apple", "pear", "apple", "orange", "lemon", "lemon", 123, True, True}
print(fruit)
# print(fruit[2]) CAN'T INDEX IT
print("pear" in fruit)
print(len(fruit))

# Break til 11:15 :)