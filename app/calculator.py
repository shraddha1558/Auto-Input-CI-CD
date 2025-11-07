import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


if __name__ == "__main__":
    # For local manual testing
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
