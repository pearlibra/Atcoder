r, c = map(int, input().split())
m = []

l1 = list(map(int, input().split()))
m.append(l1)
l2 = list(map(int, input().split()))
m.append(l2)

print(m[r-1][c-1])

