h, w = map(int, input().split())
a = [list(input()) for i in range(h)]
x = 1
y = 1

walked = [[False for i in range(500)] for j in range(500)]

for i in range(2500000):
    if walked[y - 1][x - 1]:
        print(-1)
        break
    else:
        walked[y - 1][x - 1] = True

    if a[y - 1][x - 1] == "U":
        if y == 1:
            print(y, x)
            break
        else:
            y -= 1
    elif a[y - 1][x - 1] == "D":
        if y == h:
            print(y, x)
            break
        else:
            y += 1
    elif a[y - 1][x - 1] == "L":
        if x == 1:
            print(y, x)
            break
        else:
            x -= 1
    elif a[y - 1][x - 1] == "R":
        if x == w:
            print(y, x)
            break
        else:
            x += 1
