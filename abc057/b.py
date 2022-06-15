n, m = map(int, input().split())

ab = []
cd = []

for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
for i in range(m):
    c, d = map(int, input().split())
    cd.append((c, d))

nearest_i = 0
for i in range(n):
    nearest_d = 1000000000
    for j in range(m):
        d = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if d < nearest_d:
            nearest_d = d
            nearest_i = j
    print(nearest_i + 1)