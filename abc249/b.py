s = input()

if s.islower():
    print("No")
    exit()
elif s.isupper():
    print("No")
    exit()


s = "".join(sorted(s))
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print("No")
        exit()

print("Yes")
