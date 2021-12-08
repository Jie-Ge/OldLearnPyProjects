'''
    卷积层 + 全连接层 = 16   （不包括池化层和其他层）
'''


from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Dropout,Flatten
from keras.utils import np_utils, plot_model
import numpy as np
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
x_train = x_train.reshape(-1, 32, 32, 3)/255
x_test = x_test.reshape(-1, 32, 32, 3)/255
print(x_train.shape)
print(x_test.shape)
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
print(y_train.shape)
print(y_test.shape)

model = Sequential()
# 1
model.add(Conv2D(
input_shape=(32, 32,3),
    filters=64,
    kernel_size=(3,3),
    strides=(1,1),
    padding='same',
    activation='relu',
    kernel_initializer='uniform'  # 均匀分布权重初始化
))
model.add(Conv2D(64, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(2,2)))
# 2
model.add(Conv2D(128,(3,2), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform'))
model.add(Conv2D(128,(3,3),strides=(1,1),padding='same',activation='relu',kernel_initializer='uniform'))
model.add(MaxPooling2D(pool_size=(2,2)))
# 3
model.add(Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform'))
model.add(Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform'))
model.add((Conv2D(256, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((MaxPooling2D(pool_size=(2,2))))
# 4
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((MaxPooling2D(pool_size=(2,2))))
# 5
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((Conv2D(512, (3,3), strides=(1,1), padding='same', activation='relu', kernel_initializer='uniform')))
model.add((MaxPooling2D(pool_size=(2,2))))
# 6
model.add(Flatten())
model.add(Dense(4096,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
print('fit-----------------------')
# model.fit(x_train, y_train, batch_size=100, epochs=1)
#
# loss, acc = model.evaluate(x_test, y_test, batch_size=100)
#
# print('loss: ')
# print('acc: ')
model.summary()

'''
---------------Keras.application中的VGG16模型----------------
import keras 
model = keras.applications.vgg16.VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

预训练权重:
模型参数.h5文件要放在/.keras/models下，如果该目录下没有文件，将会在上一步的载入模型时自动下载！

模型预测：
from keras.preprocessing import image 
from keras.applications.imagenet_utils import preprocess_input, decode_predictions 
import numpy as np 
import time 

t0 = time.time() 
img = image.load_img('VGG_16_CAT.jpg', target_size = (224, 224)) 
x = image.img_to_array(img) # 三维（224，224，3） 
x = np.expand_dims(x, axis = 0) # 四维（1，224，224，3） 
x = preprocess_input(x) # 预处理 
print(x.shape) 
y_pred = model.predict(x)# 预测概率 
t1 = time.time() 
print("测试图：", decode_predictions(y_pred)) # 输出五个最高概率(类名, 语义概念, 预测概率) 
print("耗时：", str((t1-t0)*1000), "ms")

'''