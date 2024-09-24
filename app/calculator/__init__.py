from app.operations import addition, subtraction, multiplication, division

class Calculator:

    @staticmethod
    def create():
        return Calculator()
        
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

# Example usage:
calc = Calculator()
print(calc.addition(10, 5))       # Output: 15
print(calc.subtraction(10, 5))    # Output: 5
print(calc.multiplication(10, 5)) # Output: 50
print(calc.division(10, 5))       # Output: 2.0
