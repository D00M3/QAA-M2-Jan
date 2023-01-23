from mock_demo import multiplied_rand_num
# pip install pytest-mock

# When running a test that is mocking an object
# we pass in 'mocker'
def test_multiplied_rand_num(mocker):
    # Arrange - Arranging setting variables and values
    # mocker is our object we are mocking, mock_demo
    # patch is modifying the functionality of this obj
    mocker.patch("mock_demo.rand_num", return_value="Hello world")

    # Act
    result = multiplied_rand_num()

    # Assert
    assert result == 1000 
    
