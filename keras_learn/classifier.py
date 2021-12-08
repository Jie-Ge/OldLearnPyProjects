import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

# X shape (60,000 28x28), y shape (10,000, )
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data_of_visual pre-processing
'''
  reshape(x, -1)；
      将数据重设为x行，列数依据数据的大小来判断
      eg：
       data_of_visual=np.array([[1, 2, 3],
                     [5, 6, 7],
                     [9, 10, 11])
        data_of_visual.reshape(1, -1)
        那么， 就会变成一行，9列
'''

X_train = X_train.reshape(X_train.shape[0], -1) / 255.   # normalize， 数据是0-255
X_test = X_test.reshape(X_test.shape[0], -1) / 255.      # normalize
'''
to_categorical(y, num_classes=None, dtype='float32')
    将整型标签转为onehot, [[0,0,1,0],
                        [1,0,0,0]]
    y为int数组，num_classes为标签类别总数，大于max(y)（标签从0开始的）
    返回：如果num_classes=None，返回(行数×列数): len(y) * [max(y)+1]，否则为 len(y) * num_classes
'''
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

'''
第一段就是加入 Dense 神经层。32 是输出的维度，784 是输入的维度。 
第一层传出的数据有 32 个 feature，传给激励单元，激励函数用到的是 relu 函数。 
经过激励函数之后，就变成了非线性的数据。 
然后再把这个数据传给下一个神经层，这个 Dense 我们定义它有 10 个输出的 feature。同样的，此处不需要再定义输入的维度，因为它接收的是上一层的输出。 
接下来再输入给下面的 softmax 函数，用来分类
'''

model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# We add metrics to get more results you want to see
model.compile(optimizer=rmsprop,  # 可以是optimizer='rmsprop', 就使用默认的优化器的参数，不需上面的那句
              loss='categorical_crossentropy',  # 亦称作多类的对数损失，注意使用该目标函数时，需要将标签转化为二值序列
              metrics=['accuracy'])  # 设置需要评估的函数

print('Training ------------')
model.fit(X_train, y_train, epochs=2, batch_size=32)

print('\nTesting ------------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)