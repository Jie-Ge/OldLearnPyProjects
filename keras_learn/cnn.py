'''
 卷积层数设置：
     选最好性能的那个模型，它是几层那就设置几层。
     这个是训练数据，激活函数，梯度更新算法等多方面的影响，也不是简单就试出来的。

卷积核数目设置：
    按照16的倍数倍增，结合了gpu硬件的配置

------------------------------
1. 使用卷积层极大地减小了全连接层中的参数的数目，使学习的问题更容易
2. 使用更多强有力的规范化技术（尤其是弃权和卷积）来减小过度拟合，
3. 使用修正线性单元而不是S型神经元，来加速训练(依据经验，通常是3-5倍)，
4. 使用GPU来计算
5. 利用充分大的数据集，避免过拟合
6. 使用正确的代价函数，避免学习减速
7. 使用好的权重初始化，避免因为神经元饱和引起的学习减速
-------------------------------
步骤：
    数据处理
    模型选择
    添加层：
        卷积层
        激活层 (可以直接写在卷积层里)
        池化层
        卷积层
        激活层
        池化层
        .....
        Flatten层
        全连接层
        激活层
        全连接层
        激活层
        .....
    编译(compile)
    训练(fit)
    评估(evaluate)
'''

import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Convolution2D, Activation, MaxPooling2D, Dense, Flatten
from keras.optimizers import Adam

# np.random.seed(1337)
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# print(x_train.shape)
# print(x_test.shape)
#
# # data_of_visual pre-processing
# # [sample,channel,width,height] [样本数，通道维度(黑白图片为1，彩色的为3)， 28*28的图像]
# x_train = X_train.reshape(-1, 1, 28, 28)/255.
# x_test = X_test.reshape(-1, 1, 28, 28)/255.
# print(x_train.shape)
# print(x_test.shape)
# # 含义：参见classifier.py
# y_train = np_utils.to_categorical(y_train, num_classes=10)
# y_test = np_utils.to_categorical(y_test, num_classes=10)

import pickle

# 加载数据并处理成需要的类型及shape

def load_file(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

data1 = load_file('cifar-10-data_of_visual/data_batch_1')
data2 = load_file('cifar-10-data_of_visual/data_batch_2')
data3 = load_file('cifar-10-data_of_visual/data_batch_3')
data4 = load_file('cifar-10-data_of_visual/data_batch_4')
data5 = load_file('cifar-10-data_of_visual/data_batch_5')
x_train = np.vstack((data1['data_of_visual'],data2['data_of_visual']))
x_train = np.vstack((x_train,data3['data_of_visual']))
x_train = np.vstack((x_train,data4['data_of_visual']))
x_train = np.vstack((x_train,data5['data_of_visual']))

y_train = data1['labels']
y_train.extend(data2['labels'])
y_train.extend(data3['labels'])
y_train.extend(data4['labels'])
y_train.extend(data5['labels'])
y_train = np.array(y_train)

testdata = load_file('cifar-10-data_of_visual/test_batch')
x_test = testdata['data_of_visual']
y_test = np.array(testdata['labels'])

# 数据标准化
x_train = x_train.reshape(-1, 3,32, 32)/255
x_test = x_test.reshape(-1, 3,32, 32)/255
print(x_train.shape)
print(x_test.shape)
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
print(y_train.shape)
print(y_test.shape)



model = Sequential()

model.add(Convolution2D(
    input_shape=(3, 32, 32),
    filters=32,  # 卷积核的数目,即输出的维度，也可以理解为：32个过滤器，每一个过滤器会过滤一遍数据，得到一个特征
    kernel_size=[5, 5],  # kernel_size=5，卷积核的宽度和长度
    strides=[1,1],  # 为卷积的步长
    padding='same',  # 代表保留边界处的卷积结果,通常会导致输出shape与输入shape相同
    # activation='relu',
    data_format='channels_first',  # 以128x128的RGB图像为例，“channels_first”应将数据组织为（3,128,128）
))
model.add(Activation('relu'))

# 池化层常用的参数设置, 作用是降维
# 如果池化层的输入单元大小不是二的整数倍，一般采取边缘补零（zero-padding）的方式补成2的倍数，然后再池化
model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same',
    data_format='channels_first',
))

# Conv layer 2 output shape (64, 14, 14)
model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first'))
model.add(Activation('relu'))

# Pooling layer 2 (max pooling) output shape (64, 7, 7)
model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))

# Fully connected layer 1 input shape (64 * 7 * 7) = (3136), output shape (1024)
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

# Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(10))
model.add(Activation('softmax'))

# Another way to define your optimizer
adam = Adam(lr=1e-4)

# We add metrics to get more results you want to see
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
# Another way to train the model
model.fit(x_train, y_train, epochs=1, batch_size=64)

print('Testing ------------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(x_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)
