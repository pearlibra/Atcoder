a, b, c = map(int, input().split())

x = a % b
tmp = x
s = set()
while tmp not in s:
    s.add(tmp)
    tmp = (tmp + x) % b

if c in s:
    print("YES")
else:
    print("NO")
