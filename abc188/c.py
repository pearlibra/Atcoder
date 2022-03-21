n = int(input())

arr = list(map(int, input().split()))

ma = 0
ind = 0
sec_ma = 0

if n == 1:
    print(arr.index(min(arr))+1)
    exit()

for i, e in enumerate(arr):
    if e > ma:
        ma = e
        ind = i+1

if ind <= 2**(n-1):
    sec_ma = max(arr[2**(n-1)+1:])
    print(arr.index(sec_ma)+1)
else:
    sec_ma = max(arr[:2**(n-1)])
    print(arr.index(sec_ma)+1)