'''
- 封装就是对对象的成员进行访问限制
- 封装的3个级别
    - 公有 public
    - 私有 private
    - 受保护的 protected
    - 注意，都不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装，只能在当前类中访问 (比如一个人的秘密)
    - 方式： 在成员前面加两个下划线
    - python的私有不是真私有，是一中name mangling的改名策略，即改了一个名
- 受保护的 protect
    - 在当前类中或者子类中可以访问，但是在外部不可以访问 (比如乳名)
    - 方式： 在成员前面加一个下划线
'''

print('======== 私有 ================')

class Person():
    # name是公有的成员变量
    name = 'jie'
    # __age是私有成员变量
    __age = 18
    # __say()是私有成员方法
    def __say(self):
        pass

yueyue = Person()
print(yueyue.name)
# print(yueyue.__age)  # 因为是在外部调用私有成员，就会报错
# 可以通过className.__dict__查看有那些成员
print(Person.__dict__)
# 只不过是改了一个名，表面私有
print(yueyue._Person__age)