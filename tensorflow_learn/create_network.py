import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error

# y = Weight * x + biase
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# newaxis放在第几个位置，就会在shape里面看到相应的位置增加了一个维数
x_data = np.linspace(-1,1,300, dtype=np.float32)[:, np.newaxis]
# 噪声， 不一定在线上， 更符合真实情况
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
# y = x的平方 + b
y_data = np.square(x_data) - 0.5 + noise

# tf.placeholder()就是代表占位符，[n行， 1列]这里的None代表无论输入有多少都可以，因为输入只有一个特征，所以这里是1
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 输入层的神经元个数由输入的数据决定（这里是一个数据， 即一个神经元）
# 这里创建（1， 10， 1）神经网络

# 添加层， 第一层到第二层， （神经元的数据值， 上一层神经元个数， 下一层神经元个数）
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# 第二层到第三层，得到最后的输出值
prediction = add_layer(l1, 10, 1, activation_function=None)

# 计算预测值prediction和真实值的误差，对二者差的平方求和再取平均
# tf.reduce_sum(data_of_visual, axis): 对数据进行压缩求和， 降维处理
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

# 如何让机器学习提升它的准确率。tf.train.GradientDescentOptimizer()中的值通常都小于1，
# 这里取的是0.1，代表以0.1的学习率来最小化误差loss
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 全局变量初始化，run一下才执行
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
# 因为这里需要先查看散点图，所以要show()一次，就需要ion(). 如果不需要查看，就可以不要这两句
plt.ion()  # 打开交互模式， 使得show()过后会继续执行后面代码
plt.show()

# 让机器学习1000次。机器学习的内容是train_step,
# 用 Session 来 run 每一次 training 的数据，逐步提升神经网络的预测准确性
for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})

    if i % 50 == 0:
        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        try:
            ax.lines.remove(line[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})
        line = plt.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)  # 暂停0.1秒

# 让最后结果不会消失
plt.ioff()
plt.show()