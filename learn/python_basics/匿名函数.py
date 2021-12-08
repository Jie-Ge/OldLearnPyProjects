from functools import reduce

'''
- lambda:
    适用于“小”、“短”、调用次数少的函数
- reduce(function, iterable):
    把一个可迭代对象归并成一个结果;
    对于作为函数参数的要求： 必须有两个参数，必须有返回结果。
- map(function, iterable1,...):
    根据提供的函数对指定序列做映射;
    序列中的每一个元素作为参数调用 function 函数，返回包含每次 function 函数返回值的新列表
'''


a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, a))  # 累加
print(list(filter(lambda x: x % 2 == 0, a)))  # 过滤
print(list(map(lambda x: x + 10, a)))  # 遍历每一个数, 对数进行操作

f = lambda x: x+5
print(f(5))