import math

shape = input("Enter the shape: Triangle,Rectangle,Circle,Square:\n")

if shape == "Triangle":
    side1 = float(input("Enter the side1:\n"))
    side2 = float(input("Enter the side2:\n"))
    side3 = float(input("Enter the side3:\n"))
    perimeter = side1 + side2 + side3
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
elif shape == "Rectangle":
    length = float(input("Enter the length of a rectangle:\n"))
    width = float(input("Enter the width of a rectangle:\n"))
    perimeter = 2 * (length + width)
    area = length * width
elif shape == "Circle":
    radius = float(input("Enter the radius:\n"))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
elif shape == "Square":
    side = float(input("Enter the side:\n"))
    perimeter = 4 * side
    area = side ** 2
else:
    print("Invalid input")

print("Perimeter of the", shape, "is", perimeter)
print("Area of the ", shape, "is", area)
