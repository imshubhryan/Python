# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         if i==0 or i==num-1 or j==0 or j==num-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# num=int(input("enter the number"))
# for i in range(num+1):
#     for j in range(i):
#         if j==0 or j==i-1:
#             print("*",end=" ")
#         else:
#             if i !=num:
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#     print()

# *
# * *
# *   *
# *     *
# * * * * *

# num=int(input("enter the number"))
# for i in range(num+1):
#     for j in range(num-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


# num=int(input("enter the number"))
# for i in range(num+1):
#     for j in range(num-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         if j==0 or j==2*i-2:
#             print("*",end=" ")
#         else:
#             if i==num:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()
    
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()
# # lower pyramid
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(2*(n-i-1)-1):
#         print("*",end=" ")
#     print() 
#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         if j==0 or j==2*i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(num-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(2*(num-i-1)-1):
#         if j==0 or j==2*(num-i-1)-2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#     enter the number 6
#           *
#         *   *
#       *       *
#     *           *
#   *               *
# *                   *
#   *               *
#     *           *
#       *       *
#         *   *
#           *


# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(2*(num-i)-1):
#         print("*",end=" ")
#     print()

# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# enter the number 5
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#         *
#       * * *
#     * * * * * 
#   * * * * * * *
# * * * * * * * * *