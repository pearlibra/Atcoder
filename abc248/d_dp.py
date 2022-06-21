N = int(input())
A = list(map(int, input().split()))
Q = int(input())

m = [[0 for i in range(N + 1)]] * (N+1)

for i in range(N):
    m[i + 1] = m[i][:]
    m[i + 1][A[i]] += 1

for i in range(Q):
    l, r, x = map(int, input().split())
    print(m[r][x] - m[l - 1][x])
