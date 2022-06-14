n = int(input())
b = list(map(int, input().split()))

a_mid = []
for i in range(len(b) - 1):
    a_mid.append(min(b[i], b[i + 1]))

print(b[0] + sum(a_mid) + b[-1])
