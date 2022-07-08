N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
pre_t = 0
for i in range(1, N):
    if t[i] - pre_t < T:
        ans += t[i] - pre_t
    else:
        ans += T
    pre_t = t[i]

ans += T
print(ans)
