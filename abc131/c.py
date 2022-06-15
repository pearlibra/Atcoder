import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


a, b, c, d = map(int, input().split())

ans = b - a + 1

ans -= (b // c - a // c) + (b // d - a // d)
if a % c == 0:
    ans -= 1
elif a % d == 0:
    ans -= 1

ans += b // lcm(c, d) - a // lcm(c, d)

print(ans)
