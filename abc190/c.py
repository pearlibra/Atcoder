n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for i in range(k)]

l = [0]*n
ans = 0

for i in cd:
    l[i[0]-1] += 1
    l[i[1]-1] += 1
print(l)

for i in ab:
    if l[i[0]-1] > 0:
        print('a')
        print(i)
        print(cd)
        if l[i[1]-1] > 0:
            if i not in cd:
                ans += 1

print(ans)

