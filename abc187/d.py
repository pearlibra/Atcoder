n = int(input())
suma, sumb = 0, 0

p = []
for i in range(n):
    a, b = map(int, input().split())
    p.append([2 * a + b, a, b])
    suma += a
p = sorted(p, reverse=True)

ans = 0
for _, a, b in p:
    suma -= a
    sumb += a
    sumb += b
    ans += 1
    if suma < sumb:
        break
print(ans)
