import numpy as np

h, w = map(int, input().split())
a = []

for i in range(h):
    a.append(list(input()))

a = np.array(a)

i = 0
while i < a.shape[0]:
    if np.all(a[i] == "."):
        a = np.delete(a, i, 0)
        continue
    i += 1

i = 0
while i < a.shape[1]:
    if np.all(a[:, i] == "."):
        a = np.delete(a, i, 1)
        continue
    i += 1

for l in a:
    print(*l, sep="")
