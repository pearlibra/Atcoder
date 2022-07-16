n = int(input())
x = ""
M = 0

while n >= 4:
    x = "4" + x
    M += 8
    n -= 4

if n == 0:
    print(M)
    print(int(x))
else:
    M += 2 * n
    x = str(n) + x
    print(M)
    print(int(x))
