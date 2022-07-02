n = int(input())
a = [list(input()) * 3 for i in range(n)] * 3
ans = 0
tmp = ""

for i in range(n, 2 * n):
    for j in range(n, 2 * n):
        tmp = ""
        for k in range(n):
            tmp += a[i][j + k]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i - k][j + k]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i - k][j]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i - k][j - k]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i][j - k]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i + k][j - k]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i + k][j]
            ans = max(int(tmp), ans)
        tmp = ""
        for k in range(n):
            tmp += a[i + k][j + k]
            ans = max(int(tmp), ans)

print(ans)
