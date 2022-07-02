N, Q = map(int, input().split())
S = list(input())
rotate_cnt = 0

for i in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        rotate_cnt += x
    elif q == 2:
        print(S[x - (rotate_cnt % N) - 1])
