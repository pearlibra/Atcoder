N = int(input())

div = N // 998244353
dis = abs(998244353 * div - N)
print(dis)
