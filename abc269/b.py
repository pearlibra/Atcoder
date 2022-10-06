A = [input() for i in range(10)]

h = 0
w = 0
ul = 0
flag_w = False
flag_h = False
is_first = True
is_last = False
a, b, c, d = 0, 0, 0, 0

if A[0][0] == "#" and A[-1][-1] == "#":
    print(1, 10)
    print(1, 10)
else:
    for i in range(10):
        for j in range(10):
            if A[i][j] == "#":
                is_last = True
                flag_h = True
                flag_w = True
                if is_first:
                    a = i + 1
                    c = j + 1
                    is_first = False
                if j == 9:
                    d = 10
                    flag_w = False
            else:
                if flag_w:
                    d = j
                    flag_w = False
        if flag_w == False:
            if is_last:
                b = i + 1
                is_last = False

    print(a, b)
    print(c, d)
