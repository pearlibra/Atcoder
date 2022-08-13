from itertools import combinations
import numpy as np

h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h1)]
a = np.array(a)

h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for i in range(h2)]
b = np.array(b)

pat_h = list(combinations(range(h1), h2))
pat_w = list(combinations(range(w1), w2))

for h in pat_h:
    for w in pat_w:
        droped_mat = a[list(h), :]
        droped_mat = droped_mat[:, list(w)]
        if np.all(droped_mat == b):
            print("Yes")
            exit()

print("No")
