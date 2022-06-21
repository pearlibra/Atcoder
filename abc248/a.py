s = input()
nums = [str(i) for i in range(10)]

for n in nums:
    if n not in s:
        print(n)
