n = int(input())
s = input()

ans = 0
for i in range(len(s)):
    tmp = 0
    x = set(s[: i + 1])
    y = set(s[i + 1 :])
    for c in x:
        if c in y:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
