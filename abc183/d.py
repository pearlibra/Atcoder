n, w = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
ma = 0
for i in range(n):
    ma = max(ma, a[i][1])

w_list = [0 for i in range(ma+1)]

for array in a:
    for i in range(array[0], array[1]):
        w_list[i] += array[2]

if max(w_list) <= w:
    print('Yes')
else:
    print('No')
