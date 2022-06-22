n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ma_idxs = set()
ma = 0

for i in range(n):
    if ma < a[i]:
        ma = a[i]
        ma_idxs = set([i+1])
    elif ma == a[i]:
        ma_idxs.add(i+1)

for i in range(k):
    if b[i] in ma_idxs:
        print("Yes")
        exit()
print("No")
