import numpy as np

h, w, k = map(int, input().split())
a = np.array([list(input()) for i in range(h)])

ans = 0

for i in range(2**h):
    cp = np.array(a)
    bi = bin(i)[2:]
    bi = bi.zfill(h)
    for j in range(h):
        if int(bi[j]):
            cp[j] = np.array(["r" for i in range(w)])
    for j in range(2**w):
        cpcp = np.array(cp)
        bi = bin(j)[2:]
        bi = bi.zfill(w)
        for l in range(w):
            if int(bi[l]):
                cpcp[:, l] = "r"

        if np.count_nonzero(cpcp == "#") == k:
            ans += 1
print(ans)
