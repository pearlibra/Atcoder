s, p = map(int, input().split())
if s >= 4:
    for i in range(1,s//2):
        if i * (s-i) == p:
            print('Yes')
            exit()
    print('No')
else:
    if s == 1:
        print('No')
    elif s == 2 and p == 1:
        print('Yes')
    elif s == 2 and p != 1:
        print('No')
    elif s == 3 and p == 2:
        print('Yes')
    else:
        print('No')