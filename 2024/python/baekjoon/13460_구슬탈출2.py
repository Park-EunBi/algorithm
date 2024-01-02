from collections import deque
n, m = map(int, input().split())
# .: 빈칸, #: 장애물, o: 구멍, R: 빨간 구슬, B: 파란 구슬
board = [
    list(input())
    for _ in range(n)
]

# 파란공과 빨간공이 동시에 들어가면 실패 -> 파란공 먼저 이동
rx, ry = 0, 0
bx, by = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

# 방문체크 리스트
visited = [[rx, ry, bx, by]]

def bfs():
    # 큐 선언, 초기화
    que = deque()
    que.append((rx, ry, 0, bx, by))
    ans = -1

    # 반복 이동
    while que:
        # 방문할 곳 뽑기
        srx, sry, cnt, sbx, sby = que.popleft()

        # 이동
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nrx, nry = srx, sry
            nbx, nby = sbx, sby
            flag_blue = 0 # 파란공 골인 플래그
            blue, red = 0, 0

            # 파란공 이동
            while 1:
                # 이동 가능하면
                if board[nbx + dx][nby + dy] != '#' and board[nbx + dx][nby + dy] != 'O':
                    # 임시 위치 갱신
                    nbx += dx
                    nby += dy
                    blue += 1
                # 이동 불가 - 벽, 구멍
                else:
                    # 구멍에 들어가면 다음 턴으로 continue
                    if board[nbx + dx][nby + dy] == 'O':
                        flag_blue = 1
                    break
            if flag_blue == 1:
                continue

            # 빨간공 이동
            while 1:
                if board[nrx + dx][nry + dy] != '#' and board[nrx + dx][nry + dy] != 'O':
                    # 임시 위치 이동
                    nrx += dx
                    nry += dy
                    red += 1
                # 이동 불가 - 벽, 구멍
                else:
                    # 구멍에 들어가면 종료
                    if board[nrx + dx][nry + dy] == 'O':
                        ans = cnt + 1
                        return ans
                    break

            # 한 턴 이동 후 동일 좌표일 경우 이동 거리순으로 비교
            # 더 많이 이동한 공을 한 칸 뒤로 (더 먼 곳에서 온 공이라서)
            if (nrx, nry) == (nbx, nby):
                if blue > red:
                    nbx -= dx
                    nby -= dy
                else:
                    nrx -= dx
                    nry -= dy

            # 방문처리
            if [nrx, nry, nbx, nby] not in visited:
                # 방문한 적 없고, 10회 미만으로 이동했을 경우 큐에 추가
                if cnt + 1 < 10:
                    visited.append([nrx, nry, nbx, nby])
                    que.append((nrx, nry, cnt + 1, nbx, nby))

    return ans

print(bfs())