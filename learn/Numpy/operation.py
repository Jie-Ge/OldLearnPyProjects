import numpy as np

a = np.array([[0, 3],
              [2, 1]])
b = np.arange(4).reshape((2,2))
# print(a, '\n', b)
c1 = b ** 2  # 平方 or n次方
c2 = np.sin(b)  # 对b中的每一个元素求sin
c3 = a * b  # 对应位置相乘
c3_dot = np.dot(a, b)  # 矩阵乘法
c3_dot_2 = a.dot(b)  # 同上
c4 = np.random.random((3, 4))
# a = np.arange(2,14).reshape(3,4)
print(c4)
# axis=1表示列，axis=0表示行
# print(np.sum(a, axis=1))  # 对每一列的所有行求和 (即对各行分别求和)
# print(np.min(a))  # 也可以加维度
print(np.mean(a))  # 求平均值
print(np.argmin(a))  # 最小值的位置
print(a.argmin())  # 同上
print(np.median(a))  # 中位数