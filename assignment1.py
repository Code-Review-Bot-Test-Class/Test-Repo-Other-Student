# Missing requirement: Implement addition function
# Missing requirement: Implement multiplication function
# Missing requirement: Handle division by zero

def subtrcat(a, b):
    return a - b
    

def divide(a, b):
    return a / b

def main():
    print("🧮 Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = input("Enter the first number (or 'q' to quit): ")
        
        if num1.lower() == 'q':
            print("Goodbye!")
            break
        
        num2 = input("Enter the second number: ")
        operator = input("Enter an operator (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid number. Try again.\n")
            continue

        if operator == '+':
            result = add(num1, num2)  # AI Review: 'add' function is not defined
        elif operator == '-':
            result = subtract(num1, num2)  # AI Review: 'subtract' function is not defined, should be 'subtrcat'
        
        elif operator == '/':
            result = divide(num1, num2)  # AI Review: Division by zero not handled
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress: 25% (only subtraction and division implemented, addition and multiplication missing, and no error handling for division by zero)