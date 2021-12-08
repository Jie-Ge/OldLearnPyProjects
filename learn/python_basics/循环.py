import random
number = random.randint(1,10)
temp = input("输入一个数字：")
guess = int(temp)
errorCount = 1
while guess != number:
    if errorCount == 3:
        print("你输入的错误次数过多，拜拜")
        break
    temp = input("error,请重新输入一个数字：")
    guess = int(temp)
    if guess == number:
        print("对了")
    else:
        errorCount = errorCount + 1
        if guess > number:
            print("大了")
        else :
            print("小了")
print("游戏结束")
print(r'C:\asda\adas\asd')
