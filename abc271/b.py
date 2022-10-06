n, q = map(int, input().split())

a = []
for i in range(n):
    landa = list(map(int, input().split()))
    nums = landa[1:]
    a.append(nums)

for i in range(q):
    s, t = map(int, input().split())
    print(a[s - 1][t - 1])
