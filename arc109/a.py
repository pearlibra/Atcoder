a,b,x,y = map(int,input().split())
if a < b:
    if 2*x <= y:
        print(2*x*(b-a) + x)
    else:
        print(x+(b-a)*y)
elif a == b:
    print(x)
else:
    if 2*x <= y:
        print(2*x*(a-b-1) + x)
    else:
        print(x + (a-b-1)*y)
