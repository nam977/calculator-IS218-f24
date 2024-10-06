from app.calculation import Addition, Subtraction, Multiplication, Division
from app.calculator import Calculator
from typing import Dict, Type
from app.history_manager import HistoryManager

# Dictionary mapping operation strings to the corresponding calculation class.
operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

class CommandProcessor:
    """
    Processes user commands, performs calculations, and interacts with the Calculator and HistoryManager.

    Attributes:
    calculator (Calculator): The calculator to perform operations.
    """
    def __init__(self) -> None:
        """Initializes the CommandProcessor with a Calculator instance."""
        self.calculator = Calculator()

    def execute(self, command: str) -> None:
        """
        Executes a given command, processes the operation, and displays the result.

        Args:
        command (str): The user's input command.
        """
        # Split the command into operation and arguments
        parts = command.split()

        # Validate input command length
        if len(parts) != 3:
            print("Invalid command format. Type 'help' for instructions.")
            return

        operation, a_str, b_str = parts

        # Convert inputs to float
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            return

        # Check if the operation is valid
        if operation not in operations_map:
            print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
            return

        # Instantiate the appropriate calculation class
        calculation_class = operations_map[operation]
        calculation = calculation_class.create(a, b)

        # Perform the calculation and print the result
        try:
            result = self.calculator.perform_operation(calculation)
            print(f"Result: {result}")
            print(f"Operation: {calculation}")  # This uses the __str__ of the calculation class
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def show_help(self) -> None:
        """Displays the help menu with available commands."""
        print("""
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  history        - Shows the operation history
  undo           - Undoes the last operation
  clear          - Clears the operation history
  exit           - Exits the REPL
  help           - Shows this help message
""")

    def show_history(self) -> None:
        """Displays the full history of operations performed."""
        history = self.calculator.get_history()
        if not history:
            print("No operations in history.")
        else:
            for index, command in enumerate(history, start=1):
                print(f"{index}: {command.operation}")

    def undo_last(self) -> None:
        """Undoes the last operation and displays the undone operation."""
        last_operation = self.calculator.undo()
        if last_operation:
            print(f"Undid operation: {last_operation.operation}")
        else:
            print("No operation to undo.")

    def clear_history(self) -> None:
        """Clears the operation history."""
        self.calculator.clear_history()
        print("History cleared.")

def main():
    processor = CommandProcessor()
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        command = input(">>> ").strip().lower()

        if command in ['exit', 'quit']:
            print("Goodbye!")
            break
        elif command == 'help':
            processor.show_help()
        elif command == 'history':
            processor.show_history()
        elif command == 'undo':
            processor.undo_last()
        elif command == 'clear':
            processor.clear_history()
        else:
            processor.execute(command)

if __name__ == '__main__':
    main()
