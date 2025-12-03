# Missing requirement: Implement addition function
# Missing requirement: Implement multiplication function
# Progress: 0% (0 out of 4 requirements met)

def subtrcat(a, b):
    return a - b
    
# AI Review: Function name is misspelled; it should be 'subtract' for clarity and correctness.
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
            # AI Review: The add function is missing; it needs to be implemented.
            result = add(num1, num2)
        elif operator == '-':
            # AI Review: The subtract function is misspelled; it should be 'subtrcat'.
            result = subtract(num1, num2)
        
        elif operator == '/':
            result = divide(num1, num2)
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")