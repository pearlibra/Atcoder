a, b, k = map(int, input().split())
ans = 0

while a * pow(k, ans) < b:
    ans += 1

print(ans)
