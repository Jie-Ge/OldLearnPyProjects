

import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='1'
# # 这是默认的显示等级，显示所有信息
# os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'
# # 只显示 warning 和 Error  
os.environ["TF_CPP_MIN_LOG_LEVEL"]='3'
# 只显示 Error  


import tensorflow as tf

state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)

# 如果定义 Variable, 就一定要 initialize
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好

# 使用 Session
# 到这里变量还是没有被激活，需要再在 sess 里, sess.run(init) , 激活 init 这一步.
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

