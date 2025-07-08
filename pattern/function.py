# def sum(a,b):
#     return a+b
# sum=sum(10,20)
# print(sum)
# 30

# def sum(list):
#     sum=0
#     for i in list:
#         sum=sum+i
#     return sum
# list=[1,2,3,4,5]
# print(sum(list))
# 15

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for i in range(10):
#     print(fibonacci(i),end=" ")

# 0 1 1 2 3 5 8 13 21 34 

# lembda function

# def hello():
#     return "Hello"
# hello=lambda:"Hello"
# print(hello())
# Hello

# sum=lambda a,b: a+b
# print(sum(1,2))
# 3

# chars=["l","c","m","d","f","y"]
# chars.sort()
# print(chars)
# chars.sort(key=lambda x:x.lower())
# print(chars)
# ['c', 'd', 'f', 'l', 'm', 'y']

# fruits = {
#   "apple": 10,
#   "banana": 20
# }
# print("Before adding new fruit:", fruits)

# # Add a new fruit
# fruits["orange"] = 30
# print("After adding new fruit:", fruits)

# Before adding new fruit: {'apple': 10, 'banana': 20}
# After adding new fruit: {'apple': 10, 'banana': 20, 'orange': 30}


# fruits = {
#   "apple": 10,
#   "banana": 20,
#   "orange": 30,
#   "grapes": 10
# }
# # 1. Using get() method
# print("Price of apple is", fruits.get("apple"))
# # 2. Using square brackets
# print("Price of banana is", fruits["banana"])

# Price of apple is 10
# Price of banana is 20