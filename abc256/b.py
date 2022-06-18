n = int(input())
a = list(map(int, input().split()))

base = [0, 0, 0, 0]
ans = 0

for hit in a:
    base[0] = 1
    for i in reversed(range(4)):
        if i + hit >= 4:
            if base[i] == 1:
                base[i] = 0
                ans += 1
        else:
            if base[i] == 1:
                base[i + hit] = 1
                base[i] = 0
print(ans)
