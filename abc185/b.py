n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]

ma = n

if n <= a[0][0]:
    print('No')
    exit()
else:
    n -= a[0][0]
    if n + a[0][1] - a[0][0] <= n:
        n += a[0][1] - a[0][0]
    else:
        n = ma
        for i in range(1,m):
            if n <= a[i][0] - a[i-1][1]:
                print('No')
                exit()
            else:
                n -= a[i][0] - a[i-1][1]
                if n + a[i][1] - a[i][0] <= n:
                    n += a[i][1] - a[i][0]
                else:
                    n = ma
        if n - (t - a[m-1][1]) > 0:
            print('Yes')
        else:
            print('No')
