l1, r1, l2, r2 = map(int, input().split())

l = min(l1, l2)
r = max(r1, r2)
cnt = 0

for i in range(l, r + 1):
    if l1 <= i <= r1 and l2 <= i <= r2:
        cnt += 1

if cnt > 1:
    print(cnt - 1)
else:
    print(0)
