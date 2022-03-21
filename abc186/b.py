h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

l_min = []

for i in a:
    l_min.append(min(i))

mi = min(l_min)

ans = 0

for i in a:
    for j in i:
        ans += j - mi

print(ans)