n, x, y = map(int, input().split())
a = list(map(int, input().split()))

h = a[::2]
v = a[1::2]

dpx = [[False for i in range(2 * 10**4 + 1)] for j in range(n + 1)]
dpx[0][10**4] = True
# print(dpx)
for i in range(len(h)):
    for k in range(2 * 10**4 + 1):
        if dpx[i][k] == True:
            if i == 0:
                dpx[i + 1][k + h[i]] = True
            else:
                dpx[i + 1][k - h[i]] = True
                dpx[i + 1][k + h[i]] = True

dpy = [[False for i in range(2 * 10**4 + 1)] for j in range(n + 1)]
dpy[0][10**4] = True

for i in range(len(v)):
    for k in range(2 * 10**4 + 1):
        if dpy[i][k] == True:
            dpy[i + 1][k - v[i]] = True
            dpy[i + 1][k + v[i]] = True

if dpx[len(h)][x + 10**4] and dpy[len(v)][y + 10**4]:
    print("Yes")
else:
    print("No")
