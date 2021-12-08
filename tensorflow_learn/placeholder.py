'''

    tf.placeholder(dtype, shape=None, name=None)
    此函数可以理解为形参，用于定义过程，在执行的时候再赋具体的值

    参数：

    dtype：数据类型。常用的是tf.float32,tf.float64等数值类型
    shape：数据形状。默认是None，就是一维值，也可以是多维，比如[2,3], [None, 3]表示列是3，行不定
    name：名称

'''


# Tensorflow 如果想要从外部传入data, 那就需要用到 tf.placeholder(),代表占位符
# 然后以这种形式传输数据 sess.run(***, feed_dict={input: **}).
# 需要传入的值放在了feed_dict={} 并一一对应每一个 input.
# placeholder 与 feed_dict={} 是绑定在一起出现的

import tensorflow as tf

import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='1'
# # 这是默认的显示等级，显示所有信息
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
# # 只显示 warning 和 Error  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error  

input1 = tf.placeholder(tf.float32)  # tensorflow一般只能处理32位的
input2 = tf.placeholder(tf.float32)

result = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(result, feed_dict={input1:[7], input2:[2]}))