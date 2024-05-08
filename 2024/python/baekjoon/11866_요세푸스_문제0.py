from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])

ans = []
while q:
    for i in range(k-1):
        q.append(q.popleft()) # 살리고
    ans.append(str(q.popleft())) # 제거하고

print('<' + ', '.join(ans) + '>')