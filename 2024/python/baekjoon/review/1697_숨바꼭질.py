from collections import deque
n, k = map(int, input().split())

def bfs():
    while q:
        x = q.popleft()
        # 종료 조건
        if x == k:
            return

        for dx in [-1, 1, x]:
            nx = x + dx
            if 0 <= nx < 1000001 and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

# main
q = deque()
q.append(n)
visited = [0 for _ in range(1000001)]
visited[n] = 0
bfs()
print(visited[k])

# a-> 2a->2a-1->2a-2보다 a->a-1->2a-2가 빠르기 때문에
# 10만보다 큰 짝수는 도중에 2배 연산을 통해 거칠 필요가 없게 된다