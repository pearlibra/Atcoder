ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())


def f(x):
    f = (cy - ay) / (cx - ax) * (x - ax) + ay
    return f


def g(x):
    g = (dy - by) / (dx - bx) * (x - bx) + by
    return g


if ax != cx:
    if (by - f(bx)) * (dy - f(dx)) > 0:
        print("No")
        exit()
    if bx != dx:
        if (ay - g(ax)) * (cy - g(cx)) > 0:
            print("No")
            exit()
    else:
        if (ax - bx) * (cx - bx) > 0:
            print("No")
            exit()
else:
    if bx != dx:
        if (ay - g(ax)) * (cy - g(cx)) > 0:
            print("No")
            exit()
    else:
        if (bx - ax) * (dx - ax) > 0:
            print("No")
            exit()
print("Yes")
