n = int(input())
ranges = []

for i in range(n):
    x, y = map(int, input().split())
    ranges.append([x, y])

ranges = sorted(ranges)
pre_r = ranges[0]

for r in ranges:
    if pre_r[1] < r[0]:
        print(*pre_r)
        pre_r = r
    elif pre_r[1] < r[1]:
        pre_r[1] = r[1]

print(*pre_r)
