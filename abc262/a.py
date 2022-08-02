y = int(input())

div4 = y%4


if div4 <= 2:
    print(y+(2-div4))
else:
    print(y+3)