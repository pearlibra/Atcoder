n, m = map(int, input().split())

b = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if b[i][j] == "#":
            yes = 0
            if j - 1 >= 0 and b[i][j - 1] == "#":
                yes = 1
            if i - 1 >= 0 and b[i - 1][j] == "#":
                yes = 1
            if j + 1 < m and b[i][j + 1] == "#":
                yes = 1
            if i + 1 < n and b[i + 1][j] == "#":
                yes = 1
            if yes == 0:
                print("No")
                exit()
print("Yes")
