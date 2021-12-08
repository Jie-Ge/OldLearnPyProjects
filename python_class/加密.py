# ord: 编码
# chr: 解码
# ( ord(s)-ord('A') + 3 ) % 26  字母相对于A的距离,再加3,取余(超出部分循环)
s = 'Z'
a = chr( ( ord(s)-ord('A') + 3 ) % 26 + ord('A') )
print(a)

