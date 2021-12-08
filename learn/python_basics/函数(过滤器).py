def firstfunction():
    '函数文档，使用Function.__doc__ 或是help(Function)可查看函数文档'
    print('调用函数不能打印函数文档')
print(firstfunction())
print(firstfunction.__doc__)
print(help(firstfunction))

# 关键字参数
def secondfunction(name, words):
    print(name + words)
secondfunction(words='dadadaaa', name='yangjie')

# 默认参数
def thirdfunction(name='jie', words='yamade'):
    print(name+words)
thirdfunction()
thirdfunction('1111', '22222')

# 收集参数(不需要知道参数的个数)或称魔法参数
def fourthfunction(*params):
    print('参数长度：', len(params))
    print('第二个参数：', params[1])
fourthfunction(1, 'jie', 3, 4, 5)

# 在函数里改变不了全局变量的值，因为在函数里会自动声明一个相同name的局部变量
# 若要改变，可加global(全局)关键字
count = 5
def fifthfunction():
    global count
    count = 10
print(count)
fifthfunction()
print(count)

# 嵌套函数
def fun1():
    print('fun1被调用')
    def fun2():
        print('fun2被调用')
    fun2() # fun2还是需要被调用才会执行
fun1()

def fun3():
    x = 5
    def fun4():
        nonlocal x  # *****
        x = x*x
        return x
    return fun4()
print(fun3())
# -----------------  匿名函数： lambda表达式 ------
def fun11(x):
    return x * 2 + 1
fun11(5)
# 以下两句与上面上句是一样的效果 
g = lambda x : x * 2 + 1 # ：前面的x是参数，：后面的是返回值
g(5)
f = lambda x, y : x * y
f(1, 2)
#----------------- 过滤器 ----------------
# filter(function or None, iterable)
# filter有两个参数，第一个是函数或者None，第二个是可迭代的数据
# None：只留下正数和True
list(filter(None, [1, 0, False, True]))
#---
def odd(x):
    return x % 2
temp = range(10) # 产生0到9十个数据
show = filter(odd, temp) # 将函数里的数据过滤掉
list(show)
# 利用匿名函数简写
list(filter(lambda x : x % 2, range(10)))
#---------------- 映射：map() --------------
# 将range(10)中的每一个数作为函数的参数
list(map(lambda x : x * 2, range(10)))



        
