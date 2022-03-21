import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
if n % 2 == 0:
    print('White')
else:
    print('Black')
