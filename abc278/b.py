H, M = map(int, input().split())

while H % 10 >= 6 or (H // 10 == 2 and M // 10 >= 4):
    M += 1
    if M == 60:
        M = 0
        H += 1
    if H == 24:
        H = 0

print(H, M)
