#Power Calculation
# x=int(input("Enter the Number-"))
# n=int(input("Enter the Number"))
# print(x ** n)


def power():
    x = float(input("Enter a number (x): "))
    n = int(input("Enter the power (n): "))
    result = 1
    for i in range(abs(n)):
        result *= x
    if n < 0:
        result = 1 / result
    print(f"{x} to the power {n} = {result}")

power()
