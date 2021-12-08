'''

LeNet-5中主要有2个卷积层、2个下抽样层（平均池化层）、3个全连接层, 最后一个全连接层做输出层

卷积层采用的都是5x5大小的卷积核/过滤器（kernel/filter），且卷积核每次滑动一个像素（stride=1）
下抽样层采用的是2x2的输入域，每次滑动2个像素

第一阶段，向前传播阶段
第二阶段，反向传播阶段
    a）算实际输出Op与相应的理想输出Yp的差；
    b）按极小化误差的方法反向传播调整权矩阵
'''


from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import SGD
from keras.utils.vis_utils import plot_model

print('start-----------------')

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 1, 28, 28)/255.
x_test = x_test.reshape(-1, 1, 28, 28)/255.

y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

print('model------------------')
model = Sequential()

model.add(Conv2D(
    input_shape=(1, 28, 28),
    filters=6,
    kernel_size=(5,5),
    strides=(1,1),
    padding='valid',
    activation='tanh',
    data_format='channels_first'
))
# LeNet网络应该用平均池化层
model.add(MaxPooling2D(pool_size=(2,2), strides=2))

model.add(Conv2D(
    filters=16,
    kernel_size=(5,5),
    strides=(1,1),
    padding='valid',
    activation='tanh',
    data_format='channels_first'
))

model.add(MaxPooling2D(pool_size=(2,2), strides=2))

model.add(Flatten())
model.add(Dense(units=120, activation='tanh'))
model.add(Dense(84, activation='tanh'))
model.add(Dense(10, activation='softmax'))

print('compile--------------------')
sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(sgd, loss='categorical_crossentropy', metrics=['accuracy'])
print('fit=========================')
model.fit(x_train, y_train, batch_size=500, epochs=1)

print('plotmodel----------------------')
plot_model(model, to_file='LeNet.png', show_shapes=True, show_layer_names=False)