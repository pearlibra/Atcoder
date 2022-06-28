h, w = map(int, input().split())

m = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if m[i][j] == ".":
            x = 0
            if i == 0:
                if j == 0:
                    x += m[i][j : j + 2].count("#")
                    x += m[i + 1][j : j + 2].count("#")
                elif j == w - 1:
                    x += m[i][j - 1 : j + 1].count("#")
                    x += m[i + 1][j - 1 : j + 1].count("#")
                else:
                    x += m[i][j - 1 : j + 2].count("#")
                    x += m[i + 1][j - 1 : j + 2].count("#")
            elif i == h - 1:
                if j == 0:
                    x += m[i][j : j + 2].count("#")
                    x += m[i - 1][j : j + 2].count("#")
                elif j == w - 1:
                    x += m[i][j - 1 : j + 1].count("#")
                    x += m[i - 1][j - 1 : j + 1].count("#")
                else:
                    x += m[i][j - 1 : j + 2].count("#")
                    x += m[i - 1][j - 1 : j + 2].count("#")
            else:
                if j == 0:
                    x += m[i - 1][j : j + 2].count("#")
                    x += m[i][j : j + 2].count("#")
                    x += m[i + 1][j : j + 2].count("#")
                elif j == w - 1:
                    x += m[i - 1][j - 1 : j + 1].count("#")
                    x += m[i][j - 1 : j + 1].count("#")
                    x += m[i + 1][j - 1 : j + 1].count("#")
                else:
                    x += m[i - 1][j - 1 : j + 2].count("#")
                    x += m[i][j - 1 : j + 2].count("#")
                    x += m[i + 1][j - 1 : j + 2].count("#")
            m[i][j] = x

for l in m:
    print(*l, sep="")
