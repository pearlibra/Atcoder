n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(sorted(a))
 
l=[[] for _ in range(k)]
 
 
for i in range(n):
    l[i%k].append(a[i])
    
for i in range(k):
    l[i] = list(sorted(l[i],reverse=True))
 
s=[]
for i in range(n):
    s.append(l[i%k].pop())
 
if all(s[i]==b[i] for i in range(n)):
    print("Yes")
else:
    print("No")