#Sum and average of all numbers in a list
mylist=[10,20,30,40,50,100]
total=0
for i in mylist:
    total += i
print("Sum=",total)
print(total / len(mylist))
