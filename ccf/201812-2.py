str1 = input()
r, y, g = str1.split()
r = int(r)
y = int(y)
g = int(g)
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
    extra = 0
    if k[i] == 2:
        s += r
        extra = r
    if k[i] != 3:
        s += t[i]
        for j in range(i+1, n):
            if k[j] == 0:
                continue
            if t[j] > t[i]:
                t[j] = t[j] - t[i]
            else:
                spend = (t[i] - t[j] + extra) % (r+y+g)
                if k[j] == 1:
                    if 0 <= spend < g:
                        k[j] = 3
                        t[j] = g - spend
                    elif g <= spend < (g+y):
                        k[j] = 2
                        t[j] = g+y-spend
                    else:
                        k[j] = 1
                        t[j] = g+y+r-spend
                elif k[j] == 3:
                    if 0 <= spend < y:
                        k[j] = 2
                        t[j] = y - spend
                    elif g <= spend < (r+y):
                        k[j] = 1
                        t[j] = r+y-spend
                    else:
                        k[j] = 3
                        t[j] = g+y+r-spend
                elif k[j] == 2:
                    if 0 <= spend < r:
                        k[j] = 1
                        t[j] = r - spend
                    elif g <= spend < (r+g):
                        k[j] = 3
                        t[j] = r+g-spend
                    else:
                        k[j] = 2
                        t[j] = g+y+r-spend
print(s)
