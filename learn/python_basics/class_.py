'''

- 类检查所有的成员
    className.__dict__

'''

print(' =============self==================== ')

# self指的是对象本身，即self=yueyue, 对象作为方法的第一个参数
# self并不是关键字， 只是用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
class Student():
    name = 'jie'  # 此属性属于类
    age = 18

    def say(self):
        self.name = 'aaaa'  # 此属性属于对象， 即yueyue的name为‘aaaa’
        self.age = 20
        print(self.name)
        print(self.age)
        print(__class__.name)

    # 当方法没有参数时，只能通过类来调用此方法
    # 通过__class__.name 来调用类的属性
    def sayAgain():
        print('sayAgain')
        print(__class__.name)
        print(__class__.age)


yueyue = Student()
yueyue.say()
Student.sayAgain()