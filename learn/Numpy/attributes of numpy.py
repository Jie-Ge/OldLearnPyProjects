import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6]])
a1 = np.zeros((3,4))  # 全为0的矩阵
# a1 = np.zeros((3,4), dtype=int64) 可定义类型
a2 = np.ones((2,3))  # 全为1的矩阵
a3 = np.empty((2,3))  #  接近于0
a4 = np.arange(10, 20, 2)  # 生成有序数列（起始数,终止数,步长）
a5 = np.arange(12).reshape((3,4))  # 生成数0-11，改变形状为3*4
a6 = np.linspace(1, 10, 5)  # 1-10 分成5段，自动匹配步长
a7 = np.linspace(1, 10, 6).reshape((2,3))  # 改变形状
print(array)
print('number of dimension:', array.ndim)  # 维数
print('shape:' , array.shape)  # 形状，几乘几
print('size:', array.size)  # 元素个数
'''
### rand()与random()相同，只是多维矩阵有无"()"的区别
### 与randn()是取数范围不一样

numpy.random.rand()  # 生成一个[0,1)之间的随机浮点数
numpy.random.rand(2) # 生成一个数列
numpy.random.rand(3, 4) # 3*4的矩阵 

numpy.random.randn() # 生成一个浮点数，取数范围：正态分布的随机样本数
numpy.random.randn(2) # 生成一个数列
numpy.random.randn(3, 4) # 3*4的矩阵

numpy.random.random()  # 生成一个[0,1)之间的随机浮点数
numpy.random.random(2) # 生成一个数列
numpy.random.random((3,4)) # 3*4的矩阵 
'''