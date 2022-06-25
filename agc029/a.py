s = input()
right = -1
ans = 0

for i, face in enumerate(s):
    if face == "W":
        ans += i - right - 1
        right += 1

print(ans)
