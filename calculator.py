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
        return "Error: Division by zero"

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero"

# Main function to perform calculations
def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    operation = input("Enter operation number (1/2/3/4/5): ")

    if operation in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif operation == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
    else:
        print("Invalid input")

# Call the calculate function to start the calculator
calculate()
