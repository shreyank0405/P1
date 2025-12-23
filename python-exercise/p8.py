#Print no 1-100, but skip the multiple of 10
num=10
for i in range(1,101):
    if i % 10 != 0:
        print(i)
    