def f(k):
    if k == 0:
        return 1
    else:
        if k in memo:
            return memo[k]
        else:
            memo[k] = f(k // 2) + f(k // 3)
            return memo[k]


memo = {}
n = int(input())

print(f(n))
