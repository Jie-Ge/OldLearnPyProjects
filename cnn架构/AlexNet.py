'''
    LeNet-5, AlexNet, ZFNet, vgg-16, GoogleNet, ResNet

'''

'''
    AlexNet网络共有：卷积层 5个，池化层 3个，全连接层：3个。  (lrn层一般很少使用了，被dropout等代替了)
    处理彩色图片

'''

from keras.datasets import cifar10
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from tensorflow.nn import lrn

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train = x_train.reshape(-1, 32, 32, 3)/255.
x_test = x_test.reshape(-1, 32, 32, 3)/255.

y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

model = Sequential()
#
model.add(Conv2D(
    input_shape=(227, 227, 3),
    filters=96,
    kernel_size=11,
    strides=4,
    padding='valid',
    activation='relu',
    kernel_initializer='uniform'  # 权重初始化， uniform：均匀分布初始化
))
model.add(MaxPooling2D(pool_size=3, strides=2, padding='valid'))
# lrn(local response normalization)： 局部响应值归一化
#       对局部神经元的活动创建竞争机制，使得其中响应比较大的值变得相对更大，
#       并抑制其他反馈较小的神经元，增强模型的泛化能力
#       对relu很管用
# 但是： 除AlexNet其他经典网络基本无LRN层，效果不明显且速度有所降低
model.add(lrn())

#
model.add(Conv2D(256, 5, strides=(1, 1), padding='same',
                 activation='relu',
                 kernel_initializer='uniform'))
model.add(MaxPooling2D((3, 3), 2))
model.add(lrn())

#
model.add(Conv2D(384, 3, padding='same',
                 activation='relu', kernel_initializer='uniform'))

#
model.add(Conv2D(384, 3, padding='same',
                 activation='relu', kernel_initializer='uniform'))

#
model.add(Conv2D(256, 3, padding='same',
                 activation='relu', kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=3, strides=2))

model.add(Flatten())
model.add(Dense(4096,activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1000, activation='softmax'))

sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(sgd, loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=500, epochs=1)

