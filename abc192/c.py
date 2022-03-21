n, k = input().split()
print(n, k)

a_i = n
g1 = sorted(n, reverse=True)
g2 = sorted(n)

print(g1, g2)

for i in range(int(k)):
    g1 = int(map(str, sorted(a_i, reverse=True)))
    g2 = int(list(str(a_i)).sort())
    a_i = str(g1 - g2)

print(a_i)