print('=======收集参数=======')
# 收集参数 也称为 魔法参数

# 好处：参数的长度可以随意
def stu(*args):
    global b
    b = 10
    print(type(args))
    for i in args:
        print(i)

stu('q', 'w', 'e')
stu('c')
stu()

print('=======收集参数之关键字参数======')


# 字典格式
def stu1(**kargs):
    print(type(kargs))
    for k, v in kargs.items():
        print(k, '---', v)


stu1(name='jie', age=18, sex='男')
stu1(name='yang')

print('========普通参数，关键字参数，收集参数的混合使用=======')


def stu2(name, age, *args, hobby='没有', **kargs):
    pass


print('========收集参数的解包问题=======')


def stu3(*args):
    print('----------')
    for i in args:
        print(type(i))
        print(i)


l = ['jie', 18, 'qwe']
# 当要传入一个列表(元组等)时，并且想要打印出列表中的每一项时，需要加*
stu3(l)
stu3(*l)

print('=========函数文档==========')


def stu4(name, age, *args):
    '''
    这里是函数的帮助文档
    :param name: 姓名
    :param age: 年龄
    :param args: 其他
    :return: 返回值
    '''
    print('这是文档')


help(stu4)
print('*' * 20)
print(stu4.__doc__)  # 更简介
