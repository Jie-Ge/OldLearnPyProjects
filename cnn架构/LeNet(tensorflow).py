'''
LeNet-5中主要有2个卷积层、2个下抽样层（平均池化层）、3个全连接层

卷积层采用的都是5x5大小的卷积核/过滤器（kernel/filter），且卷积核每次滑动一个像素（stride=1）
下抽样层采用的是2x2的输入域，每次滑动2个像素
'''

'''
    这个代码对于每层的参数选择不是很理解
    请看keras写的
'''


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

sess = tf.InteractiveSession()

def weight_variable(shape):
    # 从截断的正态分布中输出随机值
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    # 创建一个常数张量, 传入list或者数值(0.1)来填充
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
x_image = tf.reshape(x, [-1, 28, 28, 1])

print('conv1------------start------')
w_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

print('conv2------------start------')
w_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

print('fc1------------start------')
w_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

print('fc2------------start------')
w_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2) + b_fc2)

# 压缩求平均（按行或列或行列），用于降维
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_conv), reduction_indices=[1]))
# AdamOptimizer(learning_rate):寻找全局最优点
train_step = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

print('predicton--------')
# tf.equal(A, B)是对比这两个矩阵或者向量的相等的元素(逐个元素进行对比)，如果是相等的那就返回True，返回的值的矩阵维度和A是一样的
# tf.argmax(data_of_visual, axis)就是返回所在维度上最大的那个数值所在的下标
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y, 1))
# tf.cast(x,dtype,name=None)将x的数据格式转化成dtype.
# 例如，原来x的数据格式是bool， 那么将其转化成float以后，就能够将其转化成0和1的序列
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

tf.global_variables_initializer().run()
for i in range(10000):
    batch = mnist.train.next_batch(50)
    if i % 500 == 0:
        # keep_prob: dropout中设置神经元被选中的概率
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0})
        print('step %d, train_accuracy %g' % (i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})

print('test accuracy %g' % accuracy.eval(feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}))
