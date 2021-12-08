import time
t = time.clock()
print(t)
for i in range(10):
    t-=time.clock()
    print('%.2f' % -t)