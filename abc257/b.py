n, k, q = map(int, input().split())
a = list(map(int, input().split()))
L = list(map(int, input().split()))


for l in L:
    if a[l - 1] != n:
        if l < len(a):
            if a[l] != a[l - 1] + 1:
                a[l - 1] += 1
        else:
            a[l - 1] += 1
print(*a)
