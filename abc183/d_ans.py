from itertools import accumulate

n, w = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

ma = 0
for i in range(n):
    ma = max(ma, a[i][1])

w_list = [0 for i in range(ma+1)]

for array in a:
    w_list[array[0]] += array[2]
    w_list[array[1]] -= array[2]

ac = accumulate(w_list)

if max(ac) <= w:
    print('Yes')
else:
    print('No')
