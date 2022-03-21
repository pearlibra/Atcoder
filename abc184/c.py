a, b = map(int, input().split())
c, d = map(int, input().split())

if a == c and b == d:
    print(0)
elif a+b == c+d or a-b == c-d or abs(a-c) + abs(b-d) <= 3:
    print(1)
elif (a-c)%2 == (b-d)%2:
    print(2)
elif abs(abs(a-c) - abs(b-d)) <= 3:
    print(2)
else:
    print(3)