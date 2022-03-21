n, k = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(4):
    del a[i][i]

mem = a

count = 0
for i in a[0][:]:
    count += 1
    if count == 1:
        del a[2][1], a[3][1]
    elif count ==2:
        del a[1][1], a[3][2]
    elif count == 3:
        del a[1][2],a[2][2] 
    for j in a[1][:]:
    