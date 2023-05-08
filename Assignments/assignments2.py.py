"""creating methods in global area"""
import sys


def add(abc, xyz):
    """ add method"""
    return abc + xyz


def subtract(abc, xyz):
    """subtract method"""
    return abc - xyz


def multiply(abc, xyz):
    """multiply method"""
    return abc * xyz


def divide(abc, xyz):
    """divide method"""
    if xyz == 0:
        raise ValueError("Cannot divide by zero")
    return abc / xyz


def _del_():
    """delete method"""
    print("Calculator is shutting down...")


def _init_():
    print("Calculator is starting up...")


class Calculator:
    """class creation"""



# create an instance of the Calculator class
calc = Calculator()

# prompt the user for two numbers and an operation
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# perform the selected operation on the two numbers
if operation == "+":
    result = add(x, y)
elif operation == "-":
    result = subtract(x, y)
elif operation == "*":
    result = multiply(x, y)
elif operation == "/":
    try:
        result = divide(x, y)
    except ValueError as e:
        print(e)
        sys.exit()
else:
    print("Error: Invalid operation entered.")
    sys.exit()

# print out the result of the calculation
print("Result: ", result)

# destroy the Calculator object
del calc
