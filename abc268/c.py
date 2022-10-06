n = int(input())
p = list(map(int, input().split()))

happy = [0 for i in range(n)]

for i in range(n):
    happy[(p[i] - i) % n - 1] += 1
    happy[(p[i] - i) % n] += 1
    if (p[i] - i) % n + 1 < n:
        happy[(p[i] - i) % n + 1] += 1
    else:
        happy[0] += 1

print(max(happy))
