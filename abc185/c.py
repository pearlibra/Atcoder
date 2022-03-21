from math import factorial
l = int(input())

n = l -12
ans = 12**n
print(ans)
for i in range(1,n-1):
    ans /= factorial(i)**(n//i)

ans /= factorial(n)

print(int(ans))
