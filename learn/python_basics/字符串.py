print("I {1} yang {0}".format('jie', 'love'))
print("I {b} yang {a}".format(a = 'jie', b = 'love'))
#{0:.1f} 第0个位置打印一位小数
print("{0:.1f}{1}".format(23.356, 'bit'))

# 字符串格式化
print('%c' % 97) # 97转义为字符，a的ascll码是97
print('%c %c %c' % (97, 98, 99))

print('%s' % 'i love jie')
print('%d + %d = %d' % (4, 5, 4+5))
