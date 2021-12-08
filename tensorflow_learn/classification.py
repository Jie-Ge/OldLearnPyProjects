import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
MNIST库是手写体数字库,
数据中包含55000张训练图片，每张图片的分辨率是28×28，
所以我们的训练网络输入应该是28×28=784个像素数据
'''

# 读取数据，第一次会下载
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(t_xs, t_ys):
    global prediction
    # 预测y
    y_pre = sess.run(prediction, feed_dict={xs:t_xs})
    # tf.argmax(): 返回每一个向量中最大值的索引号
    # tf.equal(): 看预测值中最大值的索引号是否与真实数据的索引号相等， 返回True of False
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(t_ys, 1))
    # tf.cast(): 将correct_prediction的数据转化成tf.float32类型的， 这里是转成0,1
    # 这里因为只有0,1， 所以求平均值就是它的准确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs:t_xs, ys:t_ys})
    return result

xs = tf.placeholder(tf.float32, [None, 784])  # 28*28
ys = tf.placeholder(tf.float32, [None, 10])

prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)

# tf.reduce_sum(data_of_visual, axis): 对数据进行压缩求和， 降维处理
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for i in range(1000):
    # 每次取100个样本，不会重复取
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys:batch_ys})
    if i%50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
