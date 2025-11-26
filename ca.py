def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__== "__main__":
    x = 20
    y = 10
    print("Addition:", addition(x, y))
    print("Subtraction:", subtraction(x, y))
    print("Multiplication:", multiplication(x, y))
    print("Division:", division(x, y))