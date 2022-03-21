n, s, d = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in a:
    if i[0] < s and i[1] > d:
        print('Yes')
        exit()
print('No')