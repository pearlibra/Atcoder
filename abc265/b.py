n, m, t = map(int, input().split())
a = list(map(int, input().split()))

bonus = [0 for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    bonus[x - 1] += y

for i in range(n - 1):
    t -= a[i]
    if t <= 0:
        print("No")
        exit()
    else:
        t += bonus[i + 1]

print("Yes")
