from collections import deque
f, s, g, u, d = map(int, input().split())

def bfs():
    while q:
        now = q.popleft()
        if now == g:
            print(visited[now] - 1)
            return

        for dx in [u, -d]: # d는 음수로 전달되지 않음
            nx = now + dx
            if 1 <= nx <= f and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[now] + 1

    print('use the stairs')

q = deque()
q.append(s)
visited = [0] * (f + 1)
visited[0] = -1
visited[s] = 1 # 초깃값을 1로 설정 - 반례
bfs()

'''
3 3 1 0 1
ans: 2
'''