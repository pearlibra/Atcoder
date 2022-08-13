r, c = map(int, input().split())

d = max(abs(r - 8), abs(c - 8))

if d % 2 == 0:
    print("white")
else:
    print("black")
