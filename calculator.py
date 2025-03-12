def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

if __name__ == "__main__":
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        # Validate choice before asking for numbers
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        elif choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please select a valid option.")
            continue  # Restart the loop

        # Get user numbers only if the choice is valid
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error! Please enter valid numbers.")
            continue  # Restart the loop

        # Perform the operation
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
