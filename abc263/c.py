from itertools import combinations

n, m = map(int, input().split())

l = [i+1 for i in range(m)]

for v in combinations(l, n):
    ans = list(v)
    print(*ans, sep=' ')
