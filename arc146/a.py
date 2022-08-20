n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
cards = a[-3:]

cards = list(map(str, cards))
cards = sorted(cards)

print(*cards[::-1], sep='')
