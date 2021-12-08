#------------------------- 封装---------------------
class newclass:
    # 属性(静态的)
    name = 'jie'
    age = 20
    weight = 100
    
    # 方法（动态的）
    def eat(self):
        print('吃吃吃吃吃')
    def run(self):
        print('跑跑跑跑跑跑')
    def sleep(self):
        print('睡睡睡睡')
        
object1 = newclass() # 创建一个对象
object1.eat() # 这就是一个封装，调用类里面的eat()方法；这就像如下：
# list1 = [3, 2, 5, 4]
# list1.append(6) 调用的是python自带的一个类里面的append()方法

# ------------------------- 继承 ---------------------

class mylist(list):  # 这个类继承了list父类
    pass  # 不做处理
list1 = mylist()  # 这个类继承了list的方法和属性
list1.append(2)
list1.append(5)
list1.append(1)
print(list1)
# 多继承： class child(parent1, parent2, parent3)
# -------------------

# 如果子类中定义了与父类同名的方法或属性，则子类会覆盖父类的方法或属性
# 若还需要父类的方法或属性，可在重写的方法里加入语句：super().方法名()
class fishParent:
    def __init__(self):
        self.x = 2
        self.y = 5
    def move(self):
        self.x -= 1
        print('位置：', self.x, self.y)
        
class fishChild(fishParent):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('还要吃！！！！')
fish = fishChild()
fish.move()
        



# ------------------------- 多态 ---------------------
class A:
    def fun(self):
        print('AAAAAAAAA')
class B:
    def fun(self):
        print("BBBBBBBBB")
a = A()
b = B()
print(a.fun())
print(b.fun())  # 调用一样的方法但是结果不同

# ----------------------- self ------------------------

print('------------- self ------------------')
# self代表类的实例，而非类
# 当调用s.setName()时，实际上Python解释成Student.setName(t)，也就是说把self替换成类的实例
# 在创建实例的时候, self不需要传
# 在方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# self.name就是Student类的属性变量，是Student类所有。而name是外部传来的参数，不是Student类所自带的
# 所以，self.name = name的意思就是把外部传来的参数name的值赋值给Student类自己的属性变量self.name
class Student(object):
    __private = 'private' # 私有的
    def setName(self, name, score):
        # self.__name = name，实例的变量名如果以"__"开头,就变成了一个私有变量,只有内部可以访问,外部不能访问
        # 如果外部代码要获取name,可以给Student类增加方法
        # def get_name(self):
        #     return self.__name
        # 如果允许外部代码修改score，可以给Student类增加方法
        # def set_score(self, score):
        #     self.__score = score
        self.name = name  # self.name: 本来是没有这个属性的，是在这里添加的
        self.score = score
    def prt(self):
        print('我叫%s, 得分%s' % (self.name, self.score))
s = Student()
s.setName('yangjie', '100')
s.prt()

# ----------------- init -----------------------------

class Student(object):
    # 自带的方法__init__(),会自动调用此方法
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def prt(self):
        print('我叫%s, 得分%s' % (self.name, self.score))
s = Student('jie', '99')
# s.setName('yangjie', '100'), 就不需要这一句了
s.prt()

# ----------------  类的组合 --------------------------------

class Turtle:
    def __init__(self, x):
        self.num = x
class Fish:
    def __init__(self, x):
        self.num = x
class Pool:
    def __init__(self, x, y):
        # 实例化，self.tt是实例化对象，传入参数x初始化self.num
        self.tt = Turtle(x)
        self.fi = Fish(y)

    def prt(self):
        print('水池里有乌龟%d只，小鱼%d条' % (self.tt.num, self.fi.num))
pool = Pool(100, 200)
pool.prt()








