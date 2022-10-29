p = []
ans = 0

for i in range(9):
    s = input()
    for j in range(9):
        if s[j] == "#":
            p.append((i + 1, j + 1))

for i in range(len(p)):
    for j in range(i + 1, len(p)):
        dx = p[j][0] - p[i][0]
        dy = p[j][1] - p[i][1]
        if dx * dy < 0:
            dx = abs(dx)
            dy = abs(dy)
            if (p[i][0] + dy, p[i][1] + dx) in p and (p[j][0] + dy, p[j][1] + dx) in p:
                ans += 1

            if (p[i][0] - dy, p[i][1] - dx) in p and (
                p[j][0] - dy,
                p[j][1] - dx,
            ) in p:
                ans += 1

        else:
            dx = abs(dx)
            dy = abs(dy)
            if (p[i][0] + dy, p[i][1] - dx) in p and (p[j][0] + dy, p[j][1] - dx) in p:
                ans += 1

            if (p[i][0] - dy, p[i][1] + dx) in p and (
                p[j][0] - dy,
                p[j][1] + dx,
            ) in p:
                ans += 1


print(ans // 4)
