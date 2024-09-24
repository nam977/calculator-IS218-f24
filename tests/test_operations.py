'''My Calculator Test'''
import pytest
from app.operations import addition, subtraction, multiplication, division

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2), (2, 3, 5), (-1, -1, -2), (0, 0, 0)
])
def test_addition(a, b, expected):
    '''Addition function'''
    assert addition(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0), (-1, -1, 0), (3, 1, 2), (-5, -1, -4)
])
def test_subtraction(a, b, expected):
    '''Subtraction function'''
    assert subtraction(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1), (3, 4, 12), (-2, -4, 8), (0, 0, 0)
])
def test_multiplication(a, b, expected):
    '''Multiplication function'''
    assert multiplication(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1), (10, 5, 2), (-15, -5, 3), (-16, 4, -4)
])
def test_positive_division(a, b, expected):
    '''Positive Division function'''
    assert division(a, b) == expected

def test_negative_division():
    '''Negative Division function'''
    with pytest.raises(ZeroDivisionError):
        division(1, 0)
