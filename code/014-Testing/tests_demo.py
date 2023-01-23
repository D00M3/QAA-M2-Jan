from demo import add_hello_string
# import demo

# In order for pytest to 'see' a testing file it needs to start with tests_

def times_two(x):
    return x * 2

# Sanity testing, manually checking does this func do what I expect 
print(times_two(5)) # Gives us 10, 

# testing naming format, is test_nameOfFunc()
def test_times_two():
    # Arrange - Getting all variables and params needed
    num = 4
    result = 0

    # Act - Doing the thing we are testing
    result = times_two(num) # Expect result to be = 8

    # Assert - Checking if our act returned what we expect it to do
    assert result == 8
    # To run test `pytest ./tests_demo.py` when in same location as file

def test_add_hello_string():
    # Arrange
    word = "_test_"
    result = ""
    # Act
    result = add_hello_string(word)
    # Assert
    assert result == "hello _test_"