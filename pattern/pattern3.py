# num=int(input("enter the number"))
# for i in range(num):
#     for j in  range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(num):
#     for j in range(num-i-1):
#         print("*",end=" ")
#     print()

# enter the number 5
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



# num=int(input("enter the number"))
# for i in range(num):
#     for j in  range(num-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(num-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(num-i-1):
#         print("*",end=" ")
#     print()
# enter the number 5
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# num=int(input("enter the number"))
# for i in range(num//2,num,2):
#     for j in range(1,num-i,2):
#         print(" ",end="")
#         # fist star
#     for j in range(1,i+1,1):  
#         print("*",end="")
#         # second space
#     for j in range(1,num-i+1,1):  
#         print(" ",end="")
#         # print second star
#     for j in range(1,i+1,1):  
#         print("*",end="")
#     print()

# for i in range(num,0,-1):
#     for j in range(i, num, 1):
#         print(" ", end="")
#     for j in range(1, i*2, 1):
#         print("*", end="")
#     print()
# enter the number 6
#  ***   ***
# ***** *****
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
    
# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         if i==num//2:
#             print("*",end=" ")
#         else:
#             if j==num//2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()
#     *
#     *
# * * * * *
#     *
#     *


num=int(input("enter the number"))
for i in range(num):
    for j in range(num):
        if i==j or i+j==num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
