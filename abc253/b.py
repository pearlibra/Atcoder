h, w = map(int, input().split())

s = [input() for i in range(h)]

xy = []

for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            xy.append([i, j])

print(abs(xy[1][0] - xy[0][0]) + abs(xy[1][1] - xy[0][1]))
