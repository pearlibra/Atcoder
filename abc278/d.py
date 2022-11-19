from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

last = False
add = defaultdict(int)

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        last = query[1]
        add.clear()
    elif query[0] == 2:
        add[query[1] - 1] += query[2]
    else:
        if last != False:
            print(last + add[query[1] - 1])
        else:
            print(A[query[1] - 1] + add[query[1] - 1])
