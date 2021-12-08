from functools import reduce

'''
reduce(function, iterable):
    把一个可迭代对象归并成一个结果;
    对于作为函数参数的要求： 必须有两个参数，必须有返回结果。
'''


def fun(x, y):
    return x + y


print(reduce(fun, [1, 2, 3, 4]))

print(reduce(lambda x, y: x + y, [10, 20, 30]))
