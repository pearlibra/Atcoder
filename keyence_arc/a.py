n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ma = 0
pre = 0

l = []

for a, b in zip(a, b):
    ma = max(ma, a)
    if pre < ma * b:
        l.append(ma * b)
        pre = ma * b
    else:
        l.append(pre)

print(*l, sep='\n')

