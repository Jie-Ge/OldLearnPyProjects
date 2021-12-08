'''
- 继承就是一个类可以获得另一个类的成员属性和方法
- 在Python中，任何一个类都有一个共同的父类叫object
- 子类继承父类，那么可以使用父类除私有成员外的所有内容
- 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类方法来进行代码重用
    可以使用 “父类名.父类方法” 的格式来调用父类的方法
    也可以使用 “super().父类方法” 的格式来调用
'''

class Person():
    name = 'jie'
    age = 18

    def sleep(self):
        print('Sleeping........')

    def work(self):
        print('make some money')

# 将父类写在括号内
class Teacher(Person):
    name = 'yang'

    def make_test(self):
        print('make_test')

    def work(self):
        # 扩充父类只需要调用父类相应的函数
        # ------------ 注意加不加 self ----------------
        # 方式1: Person.work(self)
        # 方式2
        super().work()
        # self就是对象自己, self=t, 就是对象t调用成员方法, 与外部的t.work() 是一个道理
        self.make_test()


t = Teacher()
print(t.name)
print(t.age)
t.work()

print('========= 多继承 =============')

class Fish():
    def __init__(self, name):
        self.name = name  # 对象man的name属性='yueyue'

    def swim(self):
        print('swimming........')

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print('fly..........')

class SuperMan(Fish, Bird):
    pass

man = SuperMan('yueyue')
man.swim()
man.fly()
print(man.name)