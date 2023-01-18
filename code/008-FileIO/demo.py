# File IO Input Output 
# Using Python to read from files, do x with the data and modify the data in the files
# Python can be used to change .txt, .csv, .MD, 

# Opening the file and storing it as a variable fruit.txt
# fruit_file = open("fruit.txt")
# fruit_line = fruit_file.readline() # Reading the first line of the file
# print(fruit_line)

# fruit_file.close()

# Exercise - Create a file called colours.txt that contains 
# 5 colours and use Python to read and print them
# Stretch goal - Use python to print each colour on a different line 

drinks_file = open("drinks.txt")
first_line = drinks_file.readline()
print(first_line)
all_data = drinks_file.readlines()
print(all_data)
cleaned_data = []

for line in all_data:
    new_line = line.strip()
    print(new_line)
    cleaned_data.append(new_line)

print(cleaned_data)

drinks_file.close()

print("*******************************************")

orders_file = open("orders.txt")
orders_data = orders_file.readlines()
print(orders_data)

for order in orders_data: 
    new_order = order.strip()
    new_order_array = new_order.split(",")
    print(new_order_array)

orders_file.close()

# By default we open files in Read mode, open them in Append or Write
drinks_file = open("drinks.txt", "a+")
drinks_file.write("\nwater")
drinks_data = drinks_file.readlines()
print(drinks_data)
drinks_file.close()

# drinks_file = open("drinks.txt", "r")
# drinks_data = drinks_file.readlines()
# print(drinks_data)

