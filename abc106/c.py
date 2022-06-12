s = input()
k = int(input())

for i, n in enumerate(s):
    n = int(n)
    if n != 1:
        print(n)
        exit()
    else:
        if k == i+1:
            print(n)
            exit()