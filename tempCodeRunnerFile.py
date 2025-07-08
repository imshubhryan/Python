# def reverse_str(str1):
#     if len(str1)==1:
#         return str1
#     else:
#         return reverse_str(str1[1:])+str1[0]
# str1=input("Enter the string")
# str2=reverse_str(str1)
# print(str2)


num=int(input("Enter the number"))
for i in range(num):
    for j in range(i):
        print(" ",end="")
    for j in range(num-i):
        print("*",end=" ")
    print() 

