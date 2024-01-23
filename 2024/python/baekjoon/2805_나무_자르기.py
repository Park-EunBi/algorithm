import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    home = 0
    for tree in trees:
        if tree > mid:
            home += (tree - mid)
    if home < m:
        end = mid - 1
    elif home >= m:
        start = mid + 1

print(end)