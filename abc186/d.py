n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i, v in enumerate(a):
    ans += v * (n - (i + 1))
    ans -= v * i

print(ans)
