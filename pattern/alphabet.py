# num=int(input("enter the number"))
# count=0
# for i in range(num):
#     for j in range(num):
#         print(chr(65+count),end=" ")
#         count +=1
#     print()
# A B C D E
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y


# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         print(chr(65+i),end=" ")
#     print()
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E


# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num):
#         print(chr(65+j),end=" ")
#     print()
# enter the number 5
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E


# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(i+1):
#         print(chr(j+65),end=" ")
#     print()
# A
# A B
# A B C
# A B C D
# A B C D E

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(j+65),end="")
#     print()
#     A
#    AB
#   ABC
#  ABCD
# ABCDE

# num=int(input("enter the number"))
# for i in range(num):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(num-i):
#         print(chr(j+65),end=" ")
#     print()
# A B C D E
#  A B C D
#   A B C
#    A B
#     A



