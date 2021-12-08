# 辗转相除法
# a * b = 最小公约数 * 最大公倍数
a = 15
b = 10
s = a * b
while a % b != 0:
    a, b = b, (a % b)
else:
    print('最大公约数:', b)
    print('最小公倍数', s // b)
