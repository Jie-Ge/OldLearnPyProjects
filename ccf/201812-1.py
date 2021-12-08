str1 = input()
r, y, g = str1.split()
n = int(input())

k = []
t = []
for i in range(n):
    str2 = input()
    k1, t1 = str2.split()
    k.append(int(k1))
    t.append(int(t1))

s = 0
for i in range(n):
    if k[i] == 0:
        s += t[i]
    elif k[i] == 1:
        s += t[i]
    elif k[i] == 2:
        s = s + t[i] + int(r)
    else:
        continue

print(s)