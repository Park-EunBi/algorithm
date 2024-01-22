k, n = map(int, input().split())
rans = [
    int(input())
    for _ in range(k)
]

start, end = 1, max(rans)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for ran in rans:
        lines += (ran // mid)

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)