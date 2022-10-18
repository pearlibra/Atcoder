n = int(input())
a = list(map(int, input().split()))

d = {}
ans_d = {}
ans = 0

for e in a:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

for k, e in d.items():
    ans += e * (e - 1) // 2

for e in a:
    print(ans - (d[e] * (d[e] - 1)) // 2 + (d[e] - 1) * (d[e] - 2) // 2)
