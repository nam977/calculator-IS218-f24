import pytest
from app.calculator import Calculator  # assuming the class is in a file named calculator.py

# Fixture to instantiate the Calculator class
@pytest.fixture
def calculator():
    return Calculator.create()

# Parameterized tests for addition
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def test_addition(calculator, a, b, expected):
    assert calculator.addition(a, b) == expected

# Parameterized tests for subtraction
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (5, 10, -5),
    (0, 0, 0),
    (100, 50, 50)
])
def test_subtraction(calculator, a, b, expected):
    assert calculator.subtraction(a, b) == expected

# Parameterized tests for multiplication
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (0, 10, 0),
    (-1, 10, -10),
    (7, 7, 49)
])
def test_multiplication(calculator, a, b, expected):
    assert calculator.multiplication(a, b) == expected

# Parameterized tests for division, including division by zero
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2.0),
    (5, 2, 2.5),
    (-10, 5, -2.0),
    (10, 0, "Error! Division by zero.")
])
def test_division(calculator, a, b, expected):
    assert calculator.division(a, b) == expected

# Run pytest directly (if needed)
if __name__ == "__main__":
    pytest.main()
