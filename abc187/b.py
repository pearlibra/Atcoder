n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        if a[j][0] - a[i][0] == 0:
            continue
        arg = (a[j][1] - a[i][1]) / (a[j][0] - a[i][0])
        if -1 <= arg <= 1:
            ans += 1

print(ans)

