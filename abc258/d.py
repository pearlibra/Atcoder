n, x = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
cost = []
pre = 0

for i in range(n):
    if i == x:
        break
    s, g = a[i]
    cost.append(pre + s + g * (x - i))
    pre += s + g

print(min(cost))