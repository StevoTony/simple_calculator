from calculator.calculator import squareNums, triNums, lazyCaterer, magicSquares, double, negative, absoluteValue

import pytest

@pytest.mark.parametrize("function,input,expected", [
    (squareNums, 2, 4),
    (squareNums, 3, 9),
    (squareNums, 4, 16),
    (triNums, 2, 3),
    (triNums, 3, 6),
    (triNums, 4, 10),
    (lazyCaterer, 2, 4),
    (lazyCaterer, 3, 7),
    (lazyCaterer, 4, 11),
    (magicSquares, 2, 5),
    (magicSquares, 3, 15),
    (magicSquares, 4, 34),
    (double, 2, 4),
    (double, 3, 6),
    (double, 4, 8),
    (negative, 2, -2),
    (negative, 3, -3),
    (negative, 4, -4),
    (absoluteValue, 2, 2),
    (absoluteValue, -3, 3),
    (absoluteValue, -4, 4),
])
def test_everything(function, input, expected):
    assert function(input) == expected


