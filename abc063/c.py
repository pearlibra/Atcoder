n = int(input())
S = [int(input()) for i in range(n)]
not_m10 = []

for i in range(n):
    if S[i] % 10 != 0:
        not_m10.append(S[i])

s = sum(S)
if s % 10 != 0:
    print(s)
else:
    if len(not_m10) > 0:
        print(s - min(not_m10))
    else:
        print(0)
