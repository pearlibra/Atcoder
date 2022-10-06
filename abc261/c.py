n = int(input())
a = [input() for i in range(n)]

d = {}

for i, s in enumerate(a):
    if d.get(s, 0) == 0:
        d[s] = 1
        print(s)
    else:
        print(s + "({})".format(d[s]))
        d[s] += 1
