
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
    
    while True:  
        try:
            x = float(input("Enter first number: "))  
            break  
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:  
        try:
            y = float(input("Enter second number: "))  
            break  
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Addition:", add(x, y))
    print("Subtraction:", substract(x, y))   
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))         

if __name__ == "__main__":
    main()