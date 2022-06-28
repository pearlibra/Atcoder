h, w = map(int, input().split())

m = [list(input()) for i in range(h)]

dx_l = [-1, 0, 1]
dy_l = [-1, 0, 1]

for y in range(h):
    for x in range(w):
        if m[y][x] == ".":
            c = 0
            for dy in dy_l:
                for dx in dx_l:
                    xx = x + dx
                    yy = y + dy
                    
                    if xx >= 0 and xx < w and yy >= 0 and yy < h:
                        if m[yy][xx] == "#":
                            c += 1
            m[y][x] = c

for l in m:
    print(*l, sep="")
