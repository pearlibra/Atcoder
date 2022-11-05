from bisect import bisect_left

N = int(input())
P = list(map(int, input().split()))

tmp = N + 1
l = []
s = 0
end = 0

for i in range(N):
    if tmp > P[-i - 1]:
        l.append(P[-i - 1])
        tmp = P[-i - 1]
    else:
        l = sorted(l)
        s = l.pop(bisect_left(l, P[-i - 1]) - 1)

        l.append(P[-i - 1])
        l = sorted(l, reverse=True)
        end = i
        break

ans = P[: -end - 1] + [s] + l
print(*ans)
