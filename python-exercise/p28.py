#Perform List Manipulation
mylist=[10,20,30,40,50]
print("initial list=",mylist)
mylist[1]=200
print("After changing second element=",mylist)
mylist.append(600)
print("list after appending 600=",mylist)
mylist[2]=300
print("list after inserting 300 at index=",mylist)
mylist.pop(0)
print("list after removing element at index '0'=",mylist)