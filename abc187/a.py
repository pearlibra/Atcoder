l = input().split()
a = l[0]
b = l[1]

suma = 0
sumb = 0

for i in a:
    n = int(i)
    suma += n

for i in b:
    n = int(i)
    sumb += n

if suma >= sumb:
    print(suma)
else:
    print(sumb)