# [(2, 15, 1, 'Michael')]

from service import *

def test_getOne(mocker):
    # Arrange
    test_data = [(2, 15, 1, 'Michael')]
    mocker.patch("db.runQuery", return_value=[(2, 15, 1, 'Michael')])
    id = 2
    
    # Act
    result = getOne(2)

    # Assert
    assert result == test_data