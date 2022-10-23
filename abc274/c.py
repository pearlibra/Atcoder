n = int(input())
a = list(map(int, input().split()))

ans = [0, 0]

for i in range(n):
    ans.append(ans[a[i]] + 1)
    ans.append(ans[a[i]] + 1)

print(*ans[1:], sep="\n")
