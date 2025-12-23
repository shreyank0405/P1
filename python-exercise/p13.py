#Ask user to enter a word
# word=input("enter the word")
# a='aeiou'
# count=0
# for i in word:
#     if i in a:
#         count += 1
# print(count)


word=input("enter the word--")
count=0
for i in word:
    if i=='a' or 'e' or 'i' or 'o' or 'u':
        count += 1
print(count)
