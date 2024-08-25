# interpreter.py

def main():
    # Prompt the user for an arithmetic expression
    expression = input("arithmetic expression: ").strip()

    # Split the expression into components
    x, y, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the arithmetic operation
    result = calculate(x, y, z)

    # Output the result as a floating-point value formatted to one decimal place
    print(f"{result:.1f}")

def calculate(x, operator, z):
    """
    This function performs the arithmetic operation based on the operator provided.
    """
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    main()
