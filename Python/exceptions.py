import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Incorrect input value")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("error: cannot divide by zero")
    sys.exit(1)


print(f"{x}/{y} = {result}")