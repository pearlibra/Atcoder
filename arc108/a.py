import math
s, p = map(int, input().split())
if s > 2000000:
    print('No')
elif s <= 2000000 and (s+(s**2 - 4*p)**0.5)/2 % 1 == 0 and (s-(s**2 - 4*p)**0.5)/2 % 1 == 0:
    print('Yes')
else:
    print('No')