import random

def rand_num():
    return random.randint(0,10)

def multiplied_rand_num():
    return rand_num() * 2 

def createS3Bucket():
    print("making stack..")
    return True

print(multiplied_rand_num())
# Use mocking to explicityly say rand_num() returns 10
# Mocking an object / process and setting a functions return