n, k = map(int, input().split())

having_light = set(map(int, input().split()))

a = set()
for i in range(n):
    a.add(i+1)

no_light = a - having_light

xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))


distance_list = []

for nhl in list(no_light):
    d = pow(10, 11)
    for hl in list(having_light):
        d = min(d, (abs(xy[nhl-1][0] - xy[hl-1][0])**2 + abs(xy[nhl-1][1] - xy[hl-1][1])**2)**(1/2))
    distance_list.append(d)

print(max(distance_list))
