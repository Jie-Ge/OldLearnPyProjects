'''
# 模块
    - 一个模块就是一个普通py文件
    - 带入模块相当于粘贴模块的全部代码到文件中
    - 规范模块，最好在模块中编写一下内容
        - 函数(单一功能)
        - 类(相似功能的组合， 或者类似业务模块)
        - 测试代码

# 模块的使用
    - 案例 demo1
    import module_name
    module_name.function_name
    module_name.class_name
    - 或者只导入模块中一个函数或者类
        from module_name import function_name, class_name

# 模块的搜索路径和存储
    加载模块时，系统会在哪些地方寻找此模块？
    - 系统默认的搜索路径
        - 案例 demo2
        import sys
        sys.path  (获取路径列表)
    - 添加搜索路径
        sys.path.append(dir)  导入自定义模块所在的目录

# 包的导入
    - 创建： new -> Python Package
    - import package_name
    - 具体用法和模块的使用方法一样
    - 但是此方法是默认对__init__.py 文件内容的导入

    # import package.module
        - 导入包下的模块
'''


class Student():
    def __init__(self, name='NoName', age=18):
        self.name = name
        self.age = age

    def say(self):
        print('my name is {}'.format(self.name))


def sayHello():
    print('Hello.........')


if __name__ == '__main__':
    print('print...........')
