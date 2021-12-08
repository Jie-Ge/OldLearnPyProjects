# 继承中的构造函数

class Animal():
    def __init__(self):
        print('i am Animal 构造函数')

# 如果子类中有构造函数,则自动调用
class Dog(Animal):
    # __init__就是构造函数
    # 自动调用
    # 每次实例化的时候,第一个被调用
    # 主要工作是进行初始化
    def __init__(self, name):
        self.name = name  # self就是对象d, 即d的属性name='xiaohei', self.name是创建属性name
        print('i am Dog 构造函数')

# 如果子类中没有构造函数,就会在父类中查找构造函数, 没有就继续往父类的父类中查找
# 但是, 在查找构造函数过程中需要匹配相应构造函数的参数个数
class Cat(Animal):
    pass


d = Dog('xiaohei')
print(d.name)
print('-------')
c = Cat()