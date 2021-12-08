'''
闭包的定义：
    当一个函数在其内部定义函数，并且内的函数应用外部函数的参数或者局部变量，
    当内部函数被当做返回值的时候，相关参数和变量保存在返回的函数中，这种结果叫闭包
'''

def myf1(*args):

    def myf2():
        Sum = 0
        for i in args:
            Sum += i
        return Sum

    return myf2

# 调用myf1()时，myf2()没有入口，不会执行，直接执行return myf2，返回给f1
# 那么f1就是myf2，参数也会保留
f1 = myf1(1,2,3,4)
print(f1())

print('========= 闭包常见坑 =============')

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# 每一次循环都不会执行函数f(), 只会在fs中添加一个函数
# 循环3次后，fs中包含3个函数，返回给f1，f2，f3
# 然后执行这3个函数，因为循环3次后i变成了3，所以每个函数返回值都是9
f1, f2, f3 = count()
print(f1(), f2(), f3())

print('========= 解决上面的坑 ========')

def count2():
    def f(j):
        def g():
            return j*j
        return g

    fs = []
    for i in range(1, 4):
        # 使用f(i)进行传参
        fs.append(f(i))
    return fs

# 使用传参，调用函数时会保留参数
f1, f2, f3 = count2()
print(f1(), f2(), f3())