n, q = map(int, input().split())

# 数字-1(インデックス)がansの左から何番目(0から)(要素)に存在するか
state = [i for i in range(n)]

ans = [i for i in range(n)]

for i in range(q):
    x = int(input()) - 1
    if state[x] == n - 1:
        l = ans[state[x] - 1]
        ans[state[x]], ans[state[x] - 1] = (
            ans[state[x] - 1],
            ans[state[x]],
        )
        state[x] -= 1
        state[l] += 1
    else:
        r = ans[state[x] + 1]
        ans[state[x]], ans[state[x] + 1] = (
            ans[state[x] + 1],
            ans[state[x]],
        )
        state[x] += 1
        state[r] -= 1

ans = [i + 1 for i in ans]
print(*ans)
