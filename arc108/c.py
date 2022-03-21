# failed
s, p = map(int, input().split())
for i in range(1,round(p**0.5)+2):
    if i * (s-i) == p:
        print('Yes')
        exit()
print('No')