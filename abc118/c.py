n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
mi = min(a)
idx = 1

while mi > 1 and idx < len(a):
    r = a[idx] % mi
    if r < mi:
        if r != 0:
            a[idx] = mi
            mi = r
        else:
            idx += 1

print(mi)
