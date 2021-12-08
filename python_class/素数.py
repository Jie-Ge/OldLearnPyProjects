# 输入一个数,输出小于该数字的所有素数组成的集合
sushu = set()
maxnum = int(input('请输入一个自然数: '))
for num in range(2,maxnum):
    is_sushu = True
    for i in range(2, num):
        if num%i == 0:
            is_sushu = False
            break
    if is_sushu:
        sushu.add(num)
print(sushu)
