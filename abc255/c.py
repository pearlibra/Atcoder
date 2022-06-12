x, a, d, n = map(int, input().split())

if d < 0:
    d = -d
    a = -a
    x = -x

ma = a + d * (n - 1)
mi = a

if x >= ma:
    print(x - ma)
elif x <= mi:
    print(mi - x)
else:
    print(min((x - mi) % d, d - ((x - mi) % d)))
