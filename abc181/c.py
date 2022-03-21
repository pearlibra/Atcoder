import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (arr[j][0]-arr[i][0])*(arr[k][1]-arr[i][1]) == (arr[k][0]-arr[i][0])*(arr[j][1]-arr[i][1]):
                if arr[j][0]-arr[i][0] == 0 and arr[j][1]-arr[i][1]==0:
                    continue
                elif arr[k][0]-arr[i][0] ==0 and arr[k][1]-arr[i][1]==0:
                    continue
                else:
                    print('Yes')
                    exit()
            elif i == n-3 and j == n-2 and k == n-1:
                print('No')
