# str=" Simple python Code"
# print(str.split())
# print(str.split(" "))

# ['Simple', 'python', 'Code']
# ['', 'Simple', 'python', 'Code']

# str="Simple python code"
# print(str.split())
# print(str.split(" "))
# print(str.split("python"))

# ['Simple', 'python', 'code']
# ['Simple', 'python', 'code']
# ['Simple ', ' code']

# lst=[]
# word=" "
# for char in str:
#     if char !=" ":
#         word +=char
#     else:
#         lst.append(word)
#         word=" "
# lst.append(word)
# print(lst)

# str="Simple python code"
# lst=[]
# for char in str:
#     lst.append(char)
# print(lst)
# ['S', 'i', 'm', 'p', 'l', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'o', 'd', 'e']


# str="Simple python code"
# lst=[]
# for i in range(len(str)):
#     if str[i] !=" ":
#         lst.append(str[i])
#     else:
#         lst.append(" ")
# print(lst)
# ['S', 'i', 'm', 'p', 'l', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'o', 'd', 'e']

# str="Simple python code"
# lst=[char for char in str]
# print(lst)
# ['S', 'i', 'm', 'p', 'l', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n',
#   ' ', 'c', 'o', 'd', 'e']

# str="Simple python code"
# print(list(str))
# ['S', 'i', 'm', 'p', 'l', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', 
#  ' ', 'c', 'o', 'd', 'e']

# # strip() method
# str = "['Simple', 'Python', 'Code']"
# print(str.strip("[]"))
# 'Simple', 'Python', 'Code'


str = "['Simple', 'Python', 'Code']"

# strip it
str = str.strip("[]")

# # split it
# lst = str.split(", ")
# print(lst)
# print(type(lst))
# ["'Simple'", "'Python'", "'Code'"]
# <class 'list'>

# # slice assignment
# lst = []
# str = "Python"

# lst[:] = str
# print(lst)
# ['P', 'y', 't', 'h', 'o', 'n']

# # json.loads() method
# import json

# # stringified list of numbers
# str = "[1, 2, 3, 4, 5]"

# lst = json.loads(str)
# print(lst)
# print(type(lst))
# [1, 2, 3, 4, 5]
# <class 'list'>