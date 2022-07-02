k = int(input())

h = 21
m = 0
if k >= 60:
    h += 1
    k -= 60
m += k

print("{}:{:02}".format(h, m))
