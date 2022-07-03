s = input()

if s == "keyence":
    print("YES")
    exit()

for i in range(len(s) - 7):
    for j in range(len(s) - i + 1):
        removed = s[:j] + s[j + i + 1 :]
        if removed == "keyence":
            print("YES")
            exit()

print("NO")
