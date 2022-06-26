s = input()
alp = [0 for i in range(26)]
ans = 0

for i in range(2, len(s), 2):
    left = s[: i // 2]
    right = s[i // 2 : i]
    if left == right:
        ans = i

print(ans)
