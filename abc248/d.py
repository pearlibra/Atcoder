import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

idx = [[] for i in range(N + 1)]

for i in range(N):
    idx[A[i]].append(i + 1)

for i in range(Q):
    l, r, x = map(int, input().split())
    print(bisect.bisect_right(idx[x], r) - bisect.bisect_left(idx[x], l))
