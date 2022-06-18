n, k = map(int, input().split())
s = [input() for i in range(n)]
alp = "abcdefghijklmnopqrstuvwxyz"
ans = 0

for i in range(2**n):
    con = ""
    tmp = 0
    for j in range(n):
        if (i >> j) & 1:
            con += s[j]
    for a in alp:
        if con.count(a) == k:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
