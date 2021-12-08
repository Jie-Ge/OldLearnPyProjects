print('==========  __XXX__()  =========')
# 魔法方法: 当适当时机会自动触发

class A():
    name = 'yueyue'
    def __init__(self):
        print('__init__被调用')

    # 对象当做函数调用时,会调用此函数
    def __call__(self, *args, **kwargs):
        print('__call__被调用')

    # 当对象当做字符串使用时,被调用 (需返回一个字符串)
    def __str__(self):
        return '__str__被调用'

    # 当对象调用的属性不存在时, 被调用,返回None
    def __getattr__(self, item):
        print('没找到此属性')
        print(item)


a = A()  # 声明一个对象，则会自动初始化  init
a()  # 对象当做函数调用   call
print(a)  # 对象当做字符串被打印   str
print(a.arr)  # 对象调用不存在的属性  getattr