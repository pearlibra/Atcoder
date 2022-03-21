import math

n = int(input())
dots = list(map(int, input().split(" ")))

man = 0
for i in map(abs, dots):
    man += i
print(man)
s = 0
for i in dots:
    s += i**2
print(math.sqrt(s))

print(max(list(map(abs, dots))))

