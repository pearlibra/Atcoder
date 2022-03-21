n = int(input())
if n % 2 == 0:
    for i in range(n//3):
        if n % (i+1) == 0:
            print(i+1)
    print(n//2)
    print(n)
else:
    i = 0
    while i <= n // 2:
        if n % (i+1) == 0:
            print(i+1)
        i += 2
    print(n)
