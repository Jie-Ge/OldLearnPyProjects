
# Tensorboard 神经网络可视化，
# 应用create_network.py 的例子
'''
添加了：
    with tf.name_scope('layer'):
    name=''
    writer = tf.summary.FileWriter('logs/', sess.graph)  ： 保存图

'''

# (yang) yangjie@yangjie-Lenovo-XiaoXin-700-15ISK:~/anaconda3/bin$ python3 /home/yangjie/anaconda3/envs/yang/lib/python3.5/site-packages/tensorflow/tensorboard/tensorboard.py --logdir='/home/yangjie/PycharmProjects/tensorflow_learn/logs/'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error

# y = Weight * x + biase
def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]))
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1,1,300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_in')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_in')


l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

prediction = add_layer(l1, 10, 1, activation_function=None)

with tf.name_scope('loss'):
    # tf.reduce_sum(data_of_visual, axis): 对数据进行压缩求和， 降维处理
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))

with tf.name_scope('train_step'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

writer = tf.summary.FileWriter('logs/', sess.graph)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
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