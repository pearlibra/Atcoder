def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())
ans = 2
v = 1
count = 0

fac = factorization(n)


if n == 1:
    print(ans)
    exit()
elif n % 2 == 1:
    for i in fac:
        if i[0] % 2 == 1:
            count += 1
            v *= i[1]+1
        ans += 2*v
        ans -= count
else:
    for i in fac:
        if i[0] % 2 == 1:
            count += 1
            v *= i[1]+1
        ans += 2*v
        ans -= count

print(ans)
            


