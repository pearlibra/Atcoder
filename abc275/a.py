N = int(input())
H = list(map(int, input().split()))

ma = 0
ans = 0

for i in range(N):
    if ma < H[i]:
        ans = i + 1
        ma = H[i]

print(ans)

