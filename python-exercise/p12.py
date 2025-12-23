#Ask user to enter a number n
sum=0
for i in range(1,int(input("enter the number n-"))):
    if i % 2 != 0:
        sum = sum + i
print(sum)
        
