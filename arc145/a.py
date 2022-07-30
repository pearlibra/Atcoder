n = int(input())
s = list(input())

in_a = False
in_b = False

for i in range(len(s) // 2):
    l = s[i]
    r = s[-i - 1]
    if l == "A" and r == "B":
        if in_a or in_b:
            continue
        else:
            print("No")
            exit()
    if l == "B" and r == "A":
        if i == len(s) // 2 - 1 and len(s) % 2 == 0:
            if in_a or in_b:
                continue
            else:
                print("No")
                exit()
        else:
            s[i] = "A"
            in_a = True
            s[i + 1] = "B"

    if l == "A":
        in_a = True
    if r == "B":
        in_b = True

print("Yes")
