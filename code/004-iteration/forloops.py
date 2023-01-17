# For Loop is triggered x number of times 
# Range python
print(range(5)) 
print(*range(5)) # Returning the values 0, 1, 2, 3, 4
print(*range(5, 10)) # 5, 6, 7, 8, 9
print(*range(10, 0, -1)) # 10, 9, 8, 7.., 1

print(*range(5,21,2)) # Count from 5 - 20 in increases of 2
print("==============================================")
range(10) # trigger 10 times 
for x in range(10):
    print(x)

for y in range(40, -15, -7):
    print(f"Value of y is {y}")

for foobar in ["banana1", "banana2", "banana3", "banana4"]:
    print(f"Current banana is {foobar}")

snippet = ""
for num1 in range(5):
    # For every number in the loop loop through A, B, C, D
    for char1 in ["a", "b", "c", "d"]:
        result = f"{num1} : {char1}"
        # print(result)
        snippet = snippet + result

print(snippet)

