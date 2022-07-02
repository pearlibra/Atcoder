def mht_distance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy


n = int(input())
travel = [list(map(int, input().split())) for i in range(n)]
pre = [0, 0]
pre_t = 0

for i in range(n):
    t, p = travel[i][0], travel[i][1:]
    d = mht_distance(pre, p)
    if t - pre_t == d:
        pre = p
        pre_t = t
    elif t - pre_t - d > 0 and (t - pre_t - d) % 2 == 0:
        pre = p
        pre_t = t
    else:
        print("No")
        exit()

print("Yes")
