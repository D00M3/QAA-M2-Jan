from bad_code import *

def test_rolllotsofdice(mocker):
    # Use mocking to confirm that it returns 4
    # Arrange
    mocker.patch("random.randint", return_value=4)

    # Act
    result = rolllotsofdice()

    # Assert
    assert result == 4

# Exercise test checkRolls() using mocking