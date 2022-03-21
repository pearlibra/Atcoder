import sys
def input():
    return sys.stdin.readline()[:-1]

s = 0
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    s += sum(range(arr[i][0], arr[i][1]+1))

print(s)