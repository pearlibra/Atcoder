n, a, b = map(int, input().split())

if a <= b:
    print(max(0, n - a + 1))
    exit()
else:
    if n < a:
        print(0)
        exit()
    else:
        ans = 0
        div_a = n // a
        m = n % a

        if m >= b:
            ans += b
        else:
            ans += m + 1

        ans += b * (div_a - 1)

        print(ans)
