import time
'''
定义：
    在不改动函数代码的基础上无限制扩展函数功能的一种机制, 本质上是高阶函数(以函数作为参数)
使用：
    使用@语法， 即在要扩展的函数定义前使用@+函数名
'''

# 装饰器
# 打印当前时间
def printTime(f):
    def wrapper(*args, **kwargs):
        print('Time: ', time.ctime())
        return f(*args, **kwargs)
    return wrapper

@printTime
def hello():
    print('hello')

hello()

# 等同于下面的调用方式
printTime(hello)
hello()
# 即：@语法只是将函数传入装饰器函数，并无神奇之处
