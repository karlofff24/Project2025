# Buggy Calculator Example
# Created for Hacktoberfest 2025

def add(a, b):
    return a + b

def substract(a, b):   # Issue: wrong function name + incorrect logic
    return a + b       # Bug: should be a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   # Issue: no division by zero handling

def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", substract(x, y))   # Wrong function used
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))         # Will crash if y=0

if __name__ == "__main__":
    main()
