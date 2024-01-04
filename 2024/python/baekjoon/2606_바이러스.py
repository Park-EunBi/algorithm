# 1번과 연결된 컴퓨터 개수 세기
n = int(input())
v = int(input())
board = [
    []
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

for _ in range(v):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

ret = 0

def dfs(num):
    global ret
    if not visited[num]:
        visited[num] = True

    for g in board[num]:
        if not visited[g]:
            ret += 1
            dfs(g)
    return ret

# main
print(dfs(1))