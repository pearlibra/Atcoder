import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
array = list(map(int, input().split()))

goukei = 0
p = 0

for i in range(n):
    for j in array[:n+1]:
        goukei += j
        if goukei >= p:
            p = goukei

print(p)