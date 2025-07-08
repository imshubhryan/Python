# name='sachin'
# list=[10,20,3,4,5,6,5]
# tuple=(10,2.3,4.5,5)
# print(len(name))
# print(len(list))
# print(len(tuple))
# 6
# 7   length find
# 4

# print(name[0])
# print(list[4])
# print(tuple[3])
# s
# 5  select
# 5

# print(name[1:3])
# # ac slice

# print(name.count("c"))
# print(list.count(5))
# 1
# 2 count


# print(name.index("h"))
# 3 index


sum=lambda var1,var2:var1+var2
print("sum is",sum(10,20))


def func1(*mylist):
    for num in mylist:
        print(num)
    return
func1(10,20,30)
func1(2,3)
func1(1,2,3,4)
