n = int(input())
l = n

s = set()
for i in range(n):
    a = int(input())
    l = len(s)
    s.discard(a)
    if len(s) == l:
        s.add(a)

print(len(s))