N, M = map(int, input().split())
link = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in range(1, N + 1):
    print(len(link[i]), end=" ")
    print(*sorted(link[i]))
