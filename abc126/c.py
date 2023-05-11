import math


def input_sl_nums():
    return list(map(int, input().split()))


n, k = input_sl_nums()
ans = 0

for i in range(n):
    if i + 1 < k:
        ans += 1 / n * (1 / 2) ** math.ceil(math.log2(k / (i + 1)))
    else:
        ans += 1 / n

print(ans)
