n = input()
n_i = int(n)

count = 0

if n_i % 3 == 0:
    print(0)
elif n_i % 3 == 1:
    for i in n:
        if int(i) % 3 == 1:
            if len(n) > 1:
                print(1)
                exit()
    if len(n) > 2:
        print(2)
    else:
        print(-1)
else:
    for i in n:
        if int(i) % 3 == 2:
            if len(n) > 1:
                print(1)
                exit()
    if len(n) > 2:
        print(2)
    else:
        print(-1)
        

            

