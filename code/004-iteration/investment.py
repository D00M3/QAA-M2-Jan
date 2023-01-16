starting = 100
goal = int(input("Please enter goal: "))
interest = 1.1
years = 0

while starting < goal:
    starting = starting * interest
    years = years + 1

print(f"Starting with {starting}, with interest of {interest} it takes {years} years to reach {goal}")

array_fruits = ["mango", "lime", "kiwi"]
print(array_fruits[1])
char = 'a'
fruit = "apple"
print(fruit)
print(fruit[3])

word = "apple"
vowels = 0
step = 0

while step < 5:
    print(word[step])
    if word[step] == "a" or word[step] == "e" or word[step] == "i" or word[step] == "o" or word[step] == "u":
        vowels += 1
    step += 1

print(vowels)