s = input()

s_odd = s[::2]
s_even = s[1::2]

if s_odd.islower():
    if len(s) > 1 and s_even.isupper():
        print('Yes')
        exit()
    elif len(s) < 2:
        print('Yes')
        exit()

print('No')