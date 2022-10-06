N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

aj = a[-1]
count = 0
l = N
while len(a) - count > 1:
    d = a[count] % aj
    if d != 0:
        aj = d
        a.append(d)
    count += 1

print(count)