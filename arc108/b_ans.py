n = int(input())
s = input()
t = []
c = 0
 
for i in s:
    t.append(i)
    if t[-3:] == ["f","o","x"]:
        t.pop()
        t.pop()
        t.pop()
        c += 1
 
print(n-c*3)
