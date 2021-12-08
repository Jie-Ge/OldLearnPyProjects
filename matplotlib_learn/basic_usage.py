import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
# ---------------------figure1----------------------------------
plt.figure()
plt.plot(x, y1)

# ----------------------figure3---------------------------------
# 一个figure是一张图
# 指定figure的编号并指定figure的大小, 指定线的颜色, 宽度和类型
# 在这张图上绘制了两条线
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=5, linestyle='--')

# －－－－－－　下面的操作都是在plot下再进行的操作－－－－－－－－

# x轴取值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
# 设置刻度
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
# 设置刻度及刻度名称
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['really bad', 'bad', 'normal', 'good', 'really good'])
# 设置了字体为数学形式的字体，要是机器能识别的话就要加上r(正则表达的形式)以及\(识别空格)
# 使用\alpha将其转为数学的形式
# plt.yticks([-2, -1.8, -1, 1.22, 3],
#            [r'$really\ bad$', r'$bad\alpha$', r'$normal$', r'$good$', r'$really\ good$'])

ax = plt.gca()  # 'get current axis' 获取当前的坐标轴
ax.spines['right'].set_color('none')  # 去掉右边的脊梁(边框),
ax.spines['top'].set_color('none')  # 去掉上边的脊梁(边框)
# 设置坐标刻度或名称显示的位置
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
# 设置边框的位置
ax.spines['bottom'].set_position(('data_of_visual', 0))
ax.spines['left'].set_position(('data_of_visual', 0))

line1, = plt.plot(x, y2, label='up')
# 简写：plt.plot(x, y, 'r-', lw=1.0, label='down')
line2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
# 显示图例，handles:操作显示哪几条线的图例，labels:为操作的这些线重新添加标签, loc：显示的位置
# 注意：要使用handles的话，需要在对象后加‘ , ’(如上面的' line1, ')
plt.legend(handles=[line1, line2], labels=['aaa', 'bbb'], loc='best')

plt.figure(num=4)
plt.plot(x, y1)
x0 = 1
y0 = 2*x0 + 1
# 绘制一个散点（x0,y0）
plt.scatter(x0, y0, s=50, color='b')
# 绘制一条线，从(x0,x0)到(y0,0), ‘ｋ--’:简写，ｋ是黑色black, '--'是虚线，lw:线宽
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)
# (string, 需要标注的点的坐标, 标注内容的位置(以标注点为基准，横坐标加30，纵坐标减30))
plt.annotate('2x+1=3', xy=(x0, y0), xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))  # 箭头风格和弧度

plt.show()