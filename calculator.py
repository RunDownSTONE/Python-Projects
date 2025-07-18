import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number is imaginary."
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

def nth_root(x, n):
    if n == 0:
        return "Error! Cannot take 0th root."
    if x < 0 and n % 2 == 0:
        return "Error! Even root of a negative number is undefined."
    return x ** (1/n)

def logarithm(x, base):
    if x <= 0:
        return "Error! Logarithm of non-positive numbers is undefined."
    return math.log(x, base)

def percentage(x, total):
    if total == 0:
        return "Error! Cannot calculate percentage of zero."
    return (x / total) * 100

def calculator():
    print("🚀 Advanced Python Calculator 🚀")
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Cube Root")
    print("7. Nth Root")
    print("8. Logarithm")
    print("9. Percentage")
    
    while True:
        operation = input("\nEnter operation (1-9): ")
        
        if operation in ['1', '2', '3', '4']:  # Basic arithmetic operations
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Enter numeric values.")
                continue
            
            if operation == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
                
        elif operation in ['5', '6', '7']:  # Root operations
            try:
                num = float(input("Enter a number: "))
                if operation == '7':
                    n = float(input("Enter root degree (n): "))
            except ValueError:
                print("❌ Invalid input! Enter numeric values.")
                continue
            
            if operation == '5':
                result = square_root(num)
                print(f"Result: √{num} = {result}")
            elif operation == '6':
                result = cube_root(num)
                print(f"Result: ∛{num} = {result}")
            elif operation == '7':
                result = nth_root(num, n)
                print(f"Result: {n}√{num} = {result}")
        
        elif operation == '8':  # Logarithm
            try:
                num = float(input("Enter a number: "))
                base = float(input("Enter the base (default is e for natural log): ") or "math.e")
            except ValueError:
                print("❌ Invalid input! Enter numeric values.")
                continue
            
            result = logarithm(num, base)
            print(f"Result: log_{base}({num}) = {result}")
        
        elif operation == '9':  # Percentage
            try:
                part = float(input("Enter the part: "))
                total = float(input("Enter the total: "))
            except ValueError:
                print("❌ Invalid input! Enter numeric values.")
                continue
            
            result = percentage(part, total)
            print(f"Result: {part} is {result}% of {total}")
        
        else:
            print("❌ Invalid operation! Choose 1-9.")
        
        # Ask for another calculation
        another = input("\n🔹 Another calculation? (yes/no): ").lower()
        if another != 'yes':
            print("\n✨ Thank you for using the calculator! Bye! ✨")
            break

if __name__ == "__main__":
    calculator()
