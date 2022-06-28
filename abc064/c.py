n = int(input())
a = map(int, input().split())
color = set()
over = 0

for i, rate in enumerate(a):
    c = rate // 400
    if c >= 8:
        over += 1
    else:
        color.add(c)

if len(color) > 0:
    print(len(color), len(color) + over)
else:
    print(1, over)
