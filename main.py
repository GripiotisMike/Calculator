# ASCII art logo for the calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Function definitions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Dictionary to map operators to their respective functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    """Main calculator function to handle calculations."""
    print(logo)

    # Input for the first number
    num1 = float(input("What is the 1st number? : "))

    # Loop for continuous operations
    continue_calculation = True
    while continue_calculation:
        # Display available operations
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from above: ")

        # Input for the next number
        num2 = float(input("What is the next number? : "))

        # Perform the selected operation
        calculation_function = operations[operation]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        # Ask user whether to continue or start over
        choice = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = result
        else:
            continue_calculation = False
            calculator()  # Restart the calculator

# Start the calculator program
calculator()
