class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            return "cannot divide by zero"
        else:
            return self.num1 / self.num2

    def sub(self):
        return self.num1 - self.num2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
obj = Cal(num1, num2)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", obj.div(), 2)
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()
