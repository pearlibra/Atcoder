x, y, z = map(int, input().split())

if 0 < y < x:
    if z < y:
        if z < 0:
            print(-2 * z + x)
        else:
            print(x)
    else:
        print(-1)
elif x < y < 0:
    if y < z:
        if z > 0:
            print(2 * z - x)
        else:
            print(-x)
    else:
        print(-1)
else:
    print(abs(x))
