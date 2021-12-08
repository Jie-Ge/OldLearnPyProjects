import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# ---------------------  subplot 多合一显示 --------------
plt.figure(num=1)  # 一张图

# (几行， 几列， 显示在哪个位置)
plt.subplot(1, 3, 1)  # = plt.subplot(131)
plt.plot([0,1], [0,1])

qq = plt.subplot(1, 3, 2)
qq.plot([0,1], [0,2])

plt.subplot(2, 3, 3)
plt.plot([0,1], [0,3])

plt.subplot(2, 3, 6)
plt.plot([0,1], [0,4])

# ---------------------  分格显示 ------------------

# method 1: subplot2grid
plt.figure(num=2)

# 注意：坐标从0开始， 和上面的区别

# ((分成几行, 几列), (起始位置横坐标, 纵坐标), 列数)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')


# method 2: gridspec
plt.figure(num=3)

# 分成3行3列
gs = gridspec.GridSpec(3, 3)
# 占第0行所有列
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])


# method 3: subplots

# figure, 格式((图1, 图2), (图3, 图4)) = (几行, 几列, 共享x轴, 共享y轴)
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])

# 布局方式（紧凑型）
plt.tight_layout()

# ----------------------- 图中图 ---------------------------

fig = plt.figure(num=5)

# 创建数据
# 产生(1,1)(2,3)(3,4)(4,2)等坐标点
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# 大图 ： 左下角的位置以及宽度高度 = 10%, 10%, 80%, 80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')  # 注意对y进行了逆序处理
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

# ------------------------- 次坐标轴(两个y轴共享一个x轴) ------------------------

# 第一个y坐标轴
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2

fig, ax1 = plt.subplots()
ax1.plot(x, y1, 'g-')  # green, solid line
ax1.set_xlabel('X data_of_visual')
ax1.set_ylabel('Y1 data_of_visual', color='g')

# 第二个y坐标轴
ax2 = ax1.twinx()  # 就是此函数的作用，生成次坐标轴
y2 = -1 * y1
ax2.plot(x, y2, 'b-')  # blue
ax2.set_ylabel('Y2 data_of_visual', color='b')


plt.show()

