import sys

# 添加一个搜索路径
sys.path.append('/home/yangjie/PycharmProjects/learn/python/包(模块)')

# 加载模块时会在这些路径下寻找
for i in sys.path:
    print(i)