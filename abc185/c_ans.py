l = int(input())

ans = 1

for i in range(1,12):
    ans *= (l-i)/i

print(round(ans))