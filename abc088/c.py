c = [list(map(int, input().split())) for i in range(3)]

a = [0]
b = c[0] + []

a.append(c[1][0] - b[0])
a.append(c[2][0] - b[0])

for i in range(2):
    for j in range(2):
        if a[i + 1] + b[j + 1] != c[i + 1][j + 1]:
            print("No")
            exit()

print("Yes")
