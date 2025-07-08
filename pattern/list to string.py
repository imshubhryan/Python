# items=["simple","python","code"]
# str=" ".join(items)
# print(str)
# print(type(str))

# simple python code
# <class 'str'>


# items=["a","b","c","d","e"]
# str=" ".join(items)
# print(str)

# a b c d e

# items=["a","b","c","d","e"]
# str=" ".join(items)
# print(str)

# str=" , ".join(items)
# print(str)

# str="-".join(items)
# print(str)

# a b c d e
# a , b , c , d , e
# a-b-c-d-e

# items=["simple","python","code"]
# string=""
# for items in items:
#     string=string+items
# print(string)

# simplepythoncode

# items=["simple","python","code"]
# string=""
# sep=" "
# for item in items:
#     string=string+item+sep
# print(string)

# sep=","
# for item in items:
#     string=string+item+sep
# print(string)

# sep="-"
# for item in items:
#     string=string+item+sep
# print(string)

# simple python code 
# simple python code simple,python,code,
# simple python code simple,python,code,simple-python-code-


# items=[1,2,3,4,5]
# print(",".join([str(item) for item in items]))
# 1,2,3,4,5


# items=[1,2,3,4,5]
# print(",".join(map(str,items)))
# 1,2,3,4,5


# from functools import reduce
# items=["python","is","cool"]
# print(reduce(lambda a,b:a+b,items))
# pythoniscool


# import functools
# from functools import reduce

# items = ['Python', 'Is', 'Cool']
# # using reduce()
# # with separator
# print(reduce(lambda a, b: a + ' ' + b, items))
# Python Is Cool