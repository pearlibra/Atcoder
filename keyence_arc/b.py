n, k = map(int, input().split())
a = list(map(int, input().split()))

c = [0]*n
ans = 0
ceil = k

for i in a:
    c[i] += 1

for i in c:
    if ceil < i:
        ans += ceil
    else:
        ans += i
        ceil = i
    
    if ceil == 0:
        break

print(ans)

    