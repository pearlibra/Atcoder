n, x = map(int, input().split())
s = ""
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in alp:
    s += a * n

print(s[x - 1])
