N = int(input())
S = [input() for i in range(N)]

idxs = []
sec_list = []

for i in range(10):
    idxs = []
    for reel in S:
        idxs.append(reel.index(str(i)))
    idxs.sort()
    sec = 0
    tmp = 0
    for j, idx in enumerate(idxs):
        if j == 0:
            sec = idx
            tmp = idx
        elif idxs[j] == idxs[j - 1]:
            tmp += 10
            sec = max(tmp, sec)
        else:
            sec = max(sec, idx)
            tmp = idx
    sec_list.append(sec)

print(min(sec_list))
