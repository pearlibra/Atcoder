import math
a = list(map(int, input().split()))

for i in range(3):
    if 0 in a:
        a.remove(0)

ans = 0
ma = 298 - sum(a)
mi = 100 - max(a)

if mi == 1:
    mi += 1
    ans += 99*a.count(99)/sum(a)

if len(a) == 3:
    for i in range(mi, ma):
        kitai = (math.factorial(98)**3/math.factorial(a[0]-1)*math.factorial(a[1]-1)*math.factorial(a[2]-1))/(math.factorial(296)/math.factorial(sum(a)-1))
        ans += i*kitai
elif len(a) == 2:
    for i in range(mi, ma):
        kitai = (math.factorial(98)**3/math.factorial(a[0]-1)*math.factorial(a[1]-1))/(math.factorial(296)/math.factorial(sum(a)-1))
        ans += i*kitai
else:
    for i in range(mi, ma):
        kitai = (math.factorial(98)**3/math.factorial(a[0]-1))/(math.factorial(296)/math.factorial(sum(a)-1))
        ans += i*kitai

print(ans)



