n = int(input())
a = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i][j] == "W":
            if a[j][i] != "L":
                print("incorrect")
                exit()
        elif a[i][j] == "D":
            if a[j][i] != "D":
                print("incorrect")
                exit()
        elif a[i][j] == "L":
            if a[j][i] != "W":
                print("incorrect")
                exit()

print("correct")
