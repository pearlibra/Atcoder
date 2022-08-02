n, m = map(int, input().split())

a = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    a[u-1].append(v)

ans = 0

for i, l in enumerate(a):
    for j, next in enumerate(l):
        for k, next_next in enumerate(a[next-1]):
            if next_next in l:
                ans += 1

print(ans)