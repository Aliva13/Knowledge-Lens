class Calculator:
    def _init_(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2


# main program
calc = Calculator()

while True:
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", calc.add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", calc.subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", calc.multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", calc.divide(num1, num2))

    else:
        print("Invalid input")
