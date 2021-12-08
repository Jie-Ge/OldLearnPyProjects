'''
property: 定义一个property属性, 当对该属性执行相应操作时,就会引发相应事件
'''


class A():
    def __init__(self):
        self.name = 'hahah'
        self.age = 18

    def fget(self):
        print('我被读取了')
        return self.name

    def fset(self, name):
        print('我被写入了')
        self.name = 'fget' + name
        return

    def fdel(self):
        print('我被删除了')

    name2 = property(fget, fset, fdel, 'doc')


a = A()
print(a.name)
print(a.name2)
a.name2 = 'yueyue'
del a.name2
