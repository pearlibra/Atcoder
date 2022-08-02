n = int(input())
a = list(map(int, input().split()))

ans = 0
equal_cnt = 0

for i in range(n):
    if a[i] == i + 1:
        equal_cnt += 1
    elif a[i]:
        if a[a[i] - 1] == i + 1:
            ans += 1
            a[a[i] - 1] = False

ans += equal_cnt * (equal_cnt - 1) // 2
print(ans)
