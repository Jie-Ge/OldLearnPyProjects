'''
抽象类的使用：
    - 抽象类可以包含抽象方法， 也可以包含具体方法
    - 抽象类中可以有方法也可以有属性
    - 抽象类不允许实例化
    - 必须继承才可以使用， 且继承的子类必须实现所有继承来的抽象方法
    - 假定子类没有实现所有的抽象方法，则子类也不能实例化
    - 抽象类的主要作用是设定类的标准，以便于开发的时候具有统一的规范

'''

import abc


class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    # 具体方法
    def walk(self):
        print('walk........')

class Woman(Human):
    pass