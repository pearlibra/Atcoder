import math
from functools import reduce


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
A = list(map(int, input().split()))

ans = 0
gcd = my_gcd(*A)
for i in range(N):
    a = prime_factorize(A[i] / gcd)
    for e in a:
        if e != 2 and e != 3:
            print(-1)
            exit()

    ans += len(a)

print(ans)
