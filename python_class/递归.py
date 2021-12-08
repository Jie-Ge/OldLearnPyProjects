# 定义求n!的函数, 求和函数, 实现1! + 2! + ... + m!

def fact(n):
    if n == 0 :
        return 1
    return n * fact(n-1)

def sum(list2):
    a = 0
    for i in list2:
       a += i
    return a

list1 = []
num = int(input('输入一个数: '))
for i in range(num+1):
    value = fact(i)
    print(value)
    list1.append(value)
b = sum(list1)
print('1! + 2! +...+ {}! = {}'.format(num, b))