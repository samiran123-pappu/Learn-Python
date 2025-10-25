import pdb

def divide(a, b):
    pdb.set_trace()  # Set breakpoint for debugging
    result = a / b
    return result

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    try:
        print("Performing division...")
        print(f"Result: {divide(a, b)}")
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    calculator()
