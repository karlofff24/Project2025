

def add(a, b):
    return a + b

def subtract(a, b):   
    return a - b       
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"  
    return a / b

def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y)) 
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))       
if name == "main":  
    main()
