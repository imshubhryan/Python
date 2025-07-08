# num=int(input("enter the number"))
# for i in range(num+1):
#     # print left star
#     for j in range(i):
#         print("*",end="")
#         # print space
#     for j in range(2*(num-i)):
#         print(" ",end="")
#         # print right star
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end="")
#     for j in range(2*(num-i)):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
             
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
 
# -------------------------------------

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         print("*",end="")
#     print()
# *****
# *****
# *****
# *****
# *****

# ----------------------------------------------

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(num-i):
#         print("*",end=" ")
#     print()

#     enter the number 5
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# -----------------------------------------------

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
#     enter the number 5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# ---------------------------------------------------

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,num):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(num-1,i-1,-1):
#         print("*",end=" ")
#     print()
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# --------------------------------------------

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         if i==0 or i==num-1 or j==0 or j==num-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# *****
# *   *
# *   *
# *   *
# *****

# ---------------------------------------------

num=int(input("enter the number"))
for i in range(num):
    for j in range(i+1):
        x=0
        for k in range(j):
            x=x+num-k
        if j%2==0:
            print(x+i-j+1,end=" ")
        else:
            print(x+num-i,end=" ")
    print()