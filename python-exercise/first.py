#Take two number if the product of the number is less that or equal to 1000 print the product else print the sum of number
a=int(input("enter a numbre"))
b=int(input("enter a numbre"))
if a*b<=1000:
    print(a*b)
else:
    print(a+b)
print("end")