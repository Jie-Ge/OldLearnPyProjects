import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ------------ scatter 散点图 ---------------------------------
plt.figure()
n = 1024
# 正态分布(均值, 标准差,　输出的shape)
X = np.random.normal(0, 1, n)  # 每一个点的ｘ值
Y = np.random.normal(0, 1, n)  # 每一个点的ｙ值
T = np.arctan2(Y, X)  # color value

# plt.scatter(X, Y, s=75, c=T, alpha=0.5)  # alpha:透明度
plt.scatter((1,2),(3,4))  # 绘制(1,3), (2,4)两个点，　是一一对应的

# 隐藏刻度
# plt.xticks(())
# plt.yticks(())

# --------------- Bar 柱状图　--------------------------------
plt.figure()
n = 12
X = np.arange(n)  # 0 ~ 11
# 产生n个0.5~1.0的随机数
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# zip: 返回一个以元祖为元素的列表[(x1,y1), (x2,y1), (x3,y1)]
for x, y in zip(X, Y1):
    # 文本显示的位置，内容，水平对齐方式，垂直对齐方式
    plt.text(x + 0.1, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.1, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.ylim(-1.25, 1.25)

# ------------------ Contours 等高线图　-----------------------
plt.figure()

# 计算高度值
def f(x, y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 生成二维网格矩阵(x列, ｙ行)Ｘ, Y, 两个矩阵对应位置的值组成一个坐标
X, Y = np.meshgrid(x, y)

# 绘制等高线图,f: 对等高线间的填充区域进行颜色填充(x坐标, y坐标, 高度值, 把图划分成多少个区域, 透明度, 填充颜色(hot: 暖色调))
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='hot')
# 绘制等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# 为等高线添加标签
plt.clabel(C, inline=True, fontsize=10)
# plt.xticks(())
# plt.yticks(())

# ---------------------- ３Ｄ　数据　----------------------------
fig = plt.figure()
ax = Axes3D(fig)
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height valueoffset
Z = np.sin(R)

# 绘制曲面(x, y, z, 行的跨度, 列跨度, 填充颜色(rainbow: 彩虹))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# 绘制等高线图，　(x, y, x, 压缩到哪个轴, 偏移量(放在哪个位置), 填充)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2, 2)

plt.show()