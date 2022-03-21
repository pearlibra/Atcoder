n, w = map(int,input().split())

i = 0
while w * i <= n:
    i += 1

print(i-1)
