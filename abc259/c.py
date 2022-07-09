S = input()
T = input()

ls = []
lt = []
tmp = []

pre = S[0]
for i, c in enumerate(S):
    if i > 0:
        if c == S[i - 1]:
            tmp[1] += 1
        else:
            ls.append(tmp)
            tmp = [c, 1]
    else:
        tmp = [c, 1]
ls.append(tmp)

pre = T[0]
for i, c in enumerate(T):
    if i > 0:
        if c == T[i - 1]:
            tmp[1] += 1
        else:
            lt.append(tmp)
            tmp = [c, 1]
    else:
        tmp = [c, 1]
lt.append(tmp)


if len(ls) != len(lt):
    print("No")
    exit()

for i, l in enumerate(lt):
    c, n = l
    if ls[i][0] != c:
        print("No")
        exit()
    elif n > ls[i][1] and ls[i][1] < 2:
        print("No")
        exit()
    elif n < ls[i][1]:
        print("No")
        exit()

print("Yes")
