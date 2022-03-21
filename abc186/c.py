n = int(input())

a = 17
b = 15

ans = 1

while a < n:
    if str(a)[-2] == '7':
        ans += 10
    else:
        ans += 1
    a += 10

while a < n:
    if oct(a)[-2] == '7' and '7' not in str(a):
        ans += 8
    elif '7' not in str(a):
        ans += 1
    a += 8
 
print(ans)


