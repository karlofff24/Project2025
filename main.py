
def add(a, b):
    return a + b

def substract(a, b):   
    return a + b       

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   

def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", substract(x, y))   
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))         

if __name__ == "__main__":
    main()
