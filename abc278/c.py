from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(dict)


for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        d[A][B] = True
    elif T == 2:
        if B in d[A]:
            d[A].pop(B)
    else:
        if (A in d and B in d) and (B in d[A] and A in d[B]) and (d[A][B] and d[B][A]):
            print("Yes")
        else:
            print("No")
