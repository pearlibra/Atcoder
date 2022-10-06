from itertools import combinations

n = int(input())

bin_n = bin(n)
l = []

for i in range(len(bin_n) - 2):
    if (n >> i) & 1:
        l.append(2**i)

ans_list = []
for i in range(1, len(l) + 1):
    ans_list += list(combinations(l, i))

ans = []
for e in ans_list:
    ans.append(sum(e))

ans.append(0)
ans = sorted(ans)
print(*ans, sep='\n')
