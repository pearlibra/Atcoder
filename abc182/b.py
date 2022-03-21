n = int(input())
numbers = sorted(list(map(int, input().split())))

count = 0
best = 0
k = 0

for i in range(2,numbers[n-1]+1):
    for j in numbers:
        if j % i == 0:
            count += 1
    if count >= best:
        best = count
        k = i
    count = 0

print(k)




