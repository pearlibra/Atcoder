n = int(input())
s = list(input())
q = int(input())

is_q2_even = True  # クエリ2が偶数回登場した状態でTrue
first = s[:n]  # リストの前半
second = s[n:]  # リストの後半

for i in range(q):
    query = list(map(int, input().split()))
    query[1] -= 1
    query[2] -= 1

    if query[0] == 1:
        if is_q2_even:
            if query[1] >= n:
                second[query[1] - n], second[query[2] - n] = (
                    second[query[2] - n],
                    second[query[1] - n],
                )
            elif query[2] < n:
                first[query[1]], first[query[2]] = first[query[2]], first[query[1]]
            else:
                first[query[1]], second[query[2] - n] = (
                    second[query[2] - n],
                    first[query[1]],
                )
        else:
            if query[1] >= n:
                first[query[1] - n], first[query[2] - n] = (
                    first[query[2] - n],
                    first[query[1] - n],
                )
            elif query[2] < n:
                second[query[1]], second[query[2]] = second[query[2]], second[query[1]]
            else:
                second[query[1]], first[query[2] - n] = (
                    first[query[2] - n],
                    second[query[1]],
                )
    else:
        is_q2_even = not is_q2_even  # クエリ2が来た時にTFを反転


if is_q2_even:
    s = first + second
else:
    s = second + first
print(*s, sep="")
