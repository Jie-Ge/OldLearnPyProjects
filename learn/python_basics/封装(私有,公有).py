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
    - 'for 包名 import *' 禁止导入，类对象和子类可以访问
    - 方式： 在成员前面加1个下划线
- 受保护的 protect
    - 避免与子类中的属性命名冲突，无法在外部直接访问，应使用 '对象._类名__变量名' 调用
    - 方式： 在成员前面加2个下划线
'''

print('======== 私有 ================')

class Person():
    # name是公有的成员变量
    name = 'jie'
    # _age是私有成员变量
    _age = 18
    # __id 无法在外部直接访问，应使用 '对象._类名__变量名' 调用
    __id = 123
    # __say()是私有成员方法
    def __say(self):
        pass

yueyue = Person()
print(yueyue.name)
print(yueyue._age)
# print(yueyue.__id)  # 因为是在外部调用私有成员，就会报错
# 可以通过className.__dict__查看有那些成员
print(Person.__dict__)
print(yueyue._Person__id)
