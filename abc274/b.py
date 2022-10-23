h, w = map(int, input().split())
c = [input() for i in range(h)]

ans = [0 for i in range(w)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            ans[j] += 1

print(*ans)
