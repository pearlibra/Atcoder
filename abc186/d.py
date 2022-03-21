n = int(input())
l = list(map(int, input().split()))

ans = 0

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        ans += abs(l[i] - l[j])

print(ans)

