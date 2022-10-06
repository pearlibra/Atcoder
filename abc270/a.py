a, b = map(int, input().split())

if a == b:
    print(a)
elif max(a,b) == 1:
    print(1)
elif max(a, b) == 2:
    print(a + b)
elif max(a, b) == 3:
    print(3)
elif max(a, b) == 4:
    print(a + b)
elif max(a, b) == 5:
    if min(a, b) == 2 or min(a, b) == 3:
        print(7)
    else:
        print(5)
elif max(a, b) == 6:
    if min(a, b) == 1 or min(a, b) == 3:
        print(7)
    else:
        print(6)
else:
    print(7)
