#Function to create arithmatical calculation
def calculator():
    print("Arithmetic Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Operations: +, -, *, /")
    op = input("Enter operation: ")

    if op == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation!")

calculator()

