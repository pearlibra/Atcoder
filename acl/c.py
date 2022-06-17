import numpy as np
from scipy.sparse.csgraph import connected_components

n, m = map(int, input().split())

l = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    l[a][b] = 1
    l[b][a] = 1

l = np.array(l)

comps = connected_components(l, return_labels=False)

print(comps - 1)
