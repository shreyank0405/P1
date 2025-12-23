#Check the strong password
# password=int,str(input("Enter your password:-"))
# for i in password:
#     if i >= "a" or i >= "z" or i >= "A" or i >= "Z":
#         if i >= 1 or i <= 9:
#             if len(i)>=8:
#                 print(i)
#     else:
#         print("Enter a strong password") 



password=input("enter the password-")
digit=False
letter=False
for i in password:
    if i >= '0' and i <= '9':
        digit=True
    elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        letter=True
if len(password) >= 8 and letter and digit:
    print("Strong Password")
else:
    print("Weak Password")
