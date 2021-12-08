import random
import time
while True:
    print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
    time.sleep(1)
    # print(random.random())  # 产生 0 到 1 之间的随机浮点数
    print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
    # print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
    # print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
    #
    # s = 'qwertyuiop'
    # list1 = ['qwe', 'ert', 'asd', 'fer']
    # print(random.sample(list1, 2))
    # print(random.sample(s, 3))  # 从指定的序列或列表中， 随机的截取指定长度的片段
    #
    # a = [1, 3, 5, 6, 7]  # 将序列a中的元素顺序打乱
    # random.shuffle(a)
    # print(a)