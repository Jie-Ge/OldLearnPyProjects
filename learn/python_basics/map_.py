'''
map(function, iterable1,...):
    根据提供的函数对指定序列做映射;
    序列中的每一个元素作为参数调用 function 函数，返回包含每次 function 函数返回值的新列表

'''

w = map(lambda x: x ** 2, [1, 2, 3])
print(list(w))

q = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(q))

# 列表中的每个元素依次调用函数
x = [1, 3, 5, 7]
def func(w):
    return w+1

y = list(map(func, x))
print(y)