car_data = open("car_sale.csv")
car_data = car_data.readlines()

split_data = []

# Looping through our data and stripping unwanted stuff
for i in car_data:
    line = i.strip() # Getting rid of \n and stuff like that
    line_array = line.split(",") # Splitting converting strings into []
    split_data.append(line_array) # Adding the data to a new array

# Capture the data for Ford
ford_data = []
index_num = 0 
print("*******************************************")
print(split_data[1])
for x in split_data[1]:
    if index_num > 0:
        cast_data = int(x)
        ford_data.append(cast_data)
    index_num += 1

print(ford_data)
        

