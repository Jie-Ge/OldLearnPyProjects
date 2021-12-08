try:
    f = open('不存在的文件.txt')
    print(f.read())
    sum = 1 + '1'
    f.close()
# 出现异常后执行
# 文件不存在的异常属于OSError异常类型,reason是一个变量名，存储错误的原因
except OSError as reason: 
    print('文件出错了！！！\n错误的原因是：' +  str(reason))
except TypeError as reason:
    print('类型出错了！！！\n错误的原因是：' +  str(reason))
# 或者是：
# except (OSError, TypeError):
#     print('出错了')  只是这种方法不能分辨具体是哪种类型错误

# 无论如何都要执行
finally:
    # 如果上面执行的是写操作，那么遇到异常(sum=1+'1')后就不会执行f.close()语句，
    # 那么数据就不会被写进入文件 
    f.close()
