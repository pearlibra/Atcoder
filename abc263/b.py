n = int(input())
parents = list(map(int, input().split()))

p_idx = n - 2
ans = 0

while p_idx >= 0:
    p_idx = parents[p_idx] - 2
    ans += 1

print(ans)
