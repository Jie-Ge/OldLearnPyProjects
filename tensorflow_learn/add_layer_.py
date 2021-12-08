import tensorflow as tf

# y = Weight * x + biase
def add_layer(inputs, in_size, out_size, activation_function=None):

    # 因为在生成初始参数时，随机变量(normal distribution)会比全部为0要好很多，
    # 所以我们这里的weights为一个in_size行, out_size列的随机变量矩阵。
    Weight = tf.Variable(tf.random_normal([in_size, out_size]))

    # 在机器学习中，biases的推荐值不为0，所以我们这里是在0向量的基础上又加了0.1
    biase = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    # 我们定义Wx_plus_b, 即神经网络未激活的值
    Wx_plus_b = tf.multiply(Weight, inputs) + biase

    if activation_function is None:
        # 激励函数为None时，输出就是当前的预测值——Wx_plus_b
        outputs = Wx_plus_b
    else:
        # 不为None时，就把Wx_plus_b传到activation_function()函数中得到输出
        outputs = activation_function(Wx_plus_b)
    return outputs
