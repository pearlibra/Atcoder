n = int(input())

a = [list(map(int, input().split())) for i in range(2)]

ans = 0

for i in range(n):
    ans += a[0][i] * a[1][i]

if ans == 0:
    print('Yes')
else:
    print('No')