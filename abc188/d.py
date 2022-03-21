#imos methodだとメモリエラーになる
n, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ma = 0

for i in a:
    ma = max(ma, i[1])

l = [0] * (ma + 2)

for i in a:
    l[i[0]] += i[2]
    l[i[1]+1] -= i[2]

for i in range(1, len(l)):
    l[i] += l[i-1]

for i in range(len(l)):
    if l[i] > c:
        l[i] = c

print(sum(l))

# N, C = map(int, input().split())
# event = []
# for i in range(N):
#     a, b, c = map(int, input().split())
#     a -= 1

#     event.append((a, c))
#     event.append((b, -c))
# event.sort()
# ans = 0
# fee = 0
# t = 0
# for x, y in event:
#     if x != t:
#         ans += min(C, fee) * (x - t)
#         t = x
#     fee += y
# print(ans)