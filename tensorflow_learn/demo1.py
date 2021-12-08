# 一个简单的tensorflow模型

import numpy as np
import tensorflow as tf


import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='1'
# # 这是默认的显示等级，显示所有信息
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
# # 只显示 warning 和 Error  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error  


x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# 一、搭建模型

# tf.Variable: 用来创建描述 y 的参数.
# 我们可以把 y_data = x_data*0.1 + 0.3 想象成 y=Weights * x + biases,
# 然后神经网络也就是学着把 Weights 变成 0.1, biases 变成 0.3

# 定义变量
Weight = tf.Variable(tf.random_uniform([1], -1.0, 0.1))
biases = tf.Variable(tf.zeros([1]))

y = Weight*x_data + biases

# 二、最小化误差
loss = tf.reduce_mean(tf.square(y-y_data))

# 传播误差

# 我们使用的误差传递方法是梯度下降法: Gradient Descent 让后我们使用 optimizer 来进行参数的更新
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 三、训练

# 到目前为止, 我们只是建立了神经网络的结构, 还没有使用这个结构. 在使用这个结构之前, 我们必须先初始化所有之前定义的Variable, 所以这一步是很重要的!
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weight), sess.run(biases))

