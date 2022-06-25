s = input()
g_count = 0
pre_n = -1
pre_ineq = s[0]
next = 0
ans = 0

for i, ineq in enumerate(s):
    if i == 0:
        if ineq == "<":
            ans += pre_n + 1
            pre_n += 1
            pre_ineq = "<"
        else:
            g_count += 1
            pre_ineq = ">"
    else:
        if ineq == "<":
            if pre_ineq == "<":
                ans += pre_n + 1
                pre_n += 1
                pre_ineq = "<"
            else:
                if g_count - 1 < pre_n:
                    ans += (g_count - 1) * g_count // 2 + pre_n + 1
                else:
                    ans += (g_count + 1) * g_count // 2
                pre_n = 0
                g_count = 0
                pre_ineq = "<"
        else:
            g_count += 1
            pre_ineq = ">"

if pre_ineq == "<":
    ans += pre_n + 1
else:
    if g_count - 1 < pre_n:
        ans += (g_count - 1) * g_count // 2 + pre_n + 1
    else:
        ans += (g_count + 1) * g_count // 2

print(ans)
