x, y, n = map(int, input().split())

d = n // 3

if 3 * x >= y:
    print(y * d + x * (n - 3 * d))
else:
    print(x * n)
