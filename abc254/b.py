n = int(input())

out = [1]
memory = []
for i in range(1, n+1):
    for j in range(i):
        if j == i-1:
            out.append(1)
            print(1)
            memory.append(1)
        elif j == 0:
            print(1, end=' ')
            memory.append(1)
        else:
            print(out[j-1] + out[j], end=' ')
            # out[j] = out[j-1] + out[j]
            memory.append(out[j-1] + out[j])
    out = memory
    memory = []

