n = int(input())
a = list(map(int, input().split()))
c = [0 for i in range(pow(10, 5) + 2)]

for i in range(n):
    c[a[i]] += 1
    c[a[i] + 1] += 1
    c[a[i] + 2] += 1

print(max(c))
