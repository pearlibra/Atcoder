from bisect import bisect_left

n, q = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * (n + 1)
A.sort()

for i in range(n):
    C[i + 1] = C[i] + A[i]

for i in range(q):
    x = int(input())

    idx = bisect_left(A, x)
    ans = (idx * x - C[idx]) + (C[-1] - C[idx]) - (n - idx) * x
    print(ans)
