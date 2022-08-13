s = input()

a = "atcoder"
mv_count = [0 for i in range(7)]
ans = 0

for i, c in enumerate(a):
    idx = s.index(c)
    for j in range(idx):
        mv_count[j] += 1
    ans += idx - i + mv_count[idx]

print(ans)
