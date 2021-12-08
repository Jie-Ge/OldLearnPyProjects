import timeit
'''
测试代码执行时间
'''

c = '''
num = []
for i in range(1000):
    num.append(i)
'''

print(type(c))

# stmt： 要测试的代码（需要是字符串格式）
# number: 代码执行的次数
t1 = timeit.timeit(stmt='[i for i in range(1000)]', number=1000)

# 此处stmt需要的是字符串，所以将上面的代码转为字符串格式并赋给变量c
t2 = timeit.timeit(stmt=c, number=1000)

print(t1)
print(t2)

print('========== stmt跟函数(无参) ==========')

def doIt():
    num = 3
    for i in range(num):
        print('repeat for {}'.format(i))

t3 = timeit.timeit(stmt=doIt, number=2)
print(t3)

print('=========== 函数传参的情况 ===========')

q = '''
def doIt(num):
    for i in range(num):
        print('repeat for {}'.format(i))
'''

# stmt: 要执行函数
# setup: 要执行的代码及赋值变量
t4 = timeit.timeit(stmt='doIt(num)', setup=q+'num=2', number=2)
print(t4)