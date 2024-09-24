class Calculator:
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

def print_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

def get_input():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None

def main():
    calc = Calculator()
    
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            a, b = get_input()
            if a is not None and b is not None:
                print(f"Result: {calc.addition(a, b)}")
                
        elif choice == '2':
            a, b = get_input()
            if a is not None and b is not None:
                print(f"Result: {calc.subtraction(a, b)}")
                
        elif choice == '3':
            a, b = get_input()
            if a is not None and b is not None:
                print(f"Result: {calc.multiplication(a, b)}")
                
        elif choice == '4':
            a, b = get_input()
            if a is not None and b is not None:
                print(f"Result: {calc.division(a, b)}")
                
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()