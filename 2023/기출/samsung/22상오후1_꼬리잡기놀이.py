# input
n, m, k = map(int, input().split()) # 격자 크기, 팀 개수, 라운드 수
board = [[0] * (n + 1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

# 레일 위치 관리
v = [[] for _ in range(m + 1)] # 튜플로 레일 좌표 넣을 것임
# 각 팀의 tail 위치 관리
tail = [0] * (m + 1) # 팀 개수만큼
visited = [ # 격자 크기 만큼
    [False] * (n + 1)
    for _ in range(n + 1)
]

# 격자 내 레일에 각 팀 번호 작성
board_idx = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

ans = 0

# 상좌하우
dxs = [-1,  0, 1, 0]
dys = [ 0, -1, 0, 1]

def is_out_range(x, y):
    return not (1 <= x and x <= n and 1 <= y and y <= n)

# 초기 레일 만들기 - dfs

def dfs(x, y, idx):
    visited[x][y] = True
    # 팀 번호만으로 이루어진 board 작성
    board_idx[x][y] = idx # 이거 작성하려 dfs 돌리는 것
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_out_range(nx, ny): # 범위 넘어감
            continue

        # 이미 지나간 경로이거나 경로가 아닌 경우
        if board[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        # 가장 처음 탐색 시 2가 있는 방향으로 dfs 진행
        if len(v[idx]) == 1 and board[nx][ny] != 2:
            continue

        v[idx].append((nx, ny)) # 레일 저장
        if board[nx][ny] == 3: # 꼬리면
            tail[idx] = len(v[idx]) # 꼬리까지 개수
        dfs(nx, ny, idx)

# 초기 작업
def init():
    cnt = 1
    # 레일 저장, 머리사람을 앞에 넣기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 1: # 머리사람이면
                v[cnt].append((i, j)) # 머리사람의 위치 저장
                cnt += 1

    # dfs를 통해 레일을 벡터에 순서대로 넣기
    for i in range(1, m + 1):
        x, y = v[i][0] # i번 째 팀의 머리사람의 위치
        dfs(x, y, i)

# 각 팀 이동
def move_all():
    for i in range(1, m+1):
        # 레일을 한 칸씩 뒤로 이동
        tmp = v[i][-1]
        for j in range(len(v[i]) - 1, 0, -1):
            v[i][j] = v[i][j - 1]
        v[i][0] = tmp

    for i in range(1, m + 1):
        # 벡터에 저장한 정보를 바탕으로 보드 표기 변경 - 레일 이동
        for j, (x, y) in enumerate(v[i]):
            if j == 0:
                board[x][y] = 1
            elif j < tail[i] - 1:
                board[x][y] = 2
            elif j == tail[i] - 1:
                board[x][y] = 3
            else:
                board[x][y] = 4

# (x, y) 지점에 공이 닿았을 경우
def get_point(x, y):
    global ans
    idx = board_idx[x][y]
    cnt = v[idx].index((x, y))
    ans += (cnt + 1) * (cnt + 1)

# turn 번째 라운드의 공 던지기
# 공을 받은 팀원의 번호 반환
def throw_ball(turn):
    t = (turn - 1) % (4 * n) + 1 # 턴 계산

    # 1 ~ n 라운드
    # 왼 -> 오
    if t <= n:
        for i in range(1, n + 1):
            if 1 <= board[t][i] and board[t][i] <= 3:
                # 사람이 있는 첫 번째 지점 찾기
                # 점수 체크 후 팀 번호 저장
                get_point(t, i)
                return board_idx[t][i]

    # n + 1 ~ 2n 라운드
    # 아래 -> 위
    elif t <= 2 * n:
        t -= n
        for i in range(1, n+ 1):
            if 1 <= board[n + 1 -i][t] and board[n + 1 -i][t] <= 3:
                get_point(n + 1 -i, t)
                return board_idx[n + 1 -i][t]

    # 2n+1 ~ 3n 라운드
    # 오 -> 왼
    elif t <= 3 * n:
        t -= (2 * n)
        for i in range(1, n + 1):
            if 1 <= board[n + 1 -t][n + 1 -i] and board[n + 1 -t][n + 1 -i] <= 3:
                get_point(n + 1 -t, n + 1 -i)
                return board_idx[n + 1 -t][n + 1 -i]

    # 3n+1 ~ 4n 라운드
    else:
        t -= (3 * n)
        for i in range(1, n + 1):
            if 1 <= board[i][n + 1 - t] and board[i][n + 1 - t] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(i, n + 1 - t)
                return board_idx[i][n + 1 - t]

    # 공이 그대로 지나가면 0
    return 0

# 공을 획득한 팀 - 순서 변경
def reverse(i):
    # 아무도 공을 받지 못했다면 패스
    if got_ball_idx == 0:
        return

    idx = got_ball_idx

    new_v = []

    # 순서에 맞게 new_v에 레일을 넣기
    for j in range(tail[idx] - 1, -1, -1):
        new_v.append(v[idx][j])

    for j in range(len(v[idx]) -1, tail[idx] -1, -1):
        new_v.append(v[idx][j])

    v[idx] = new_v[:]

    # 벡터에 저장한 정보를 바탕으로 보드 표기 변경
    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            board[x][y] = 1
        elif j < tail[idx] -1:
            board[x][y] = 2
        elif j == tail[idx] -1:
            board[x][y] = 3
        else:
            board[x][y] = 4

# main
init()
for i in range(1, k + 1):
    # 머리사람을 따라 한 칸씩 이동
    move_all()

    # i 번째 라운드의 공 던지기, 점수 부여
    got_ball_idx = throw_ball(i)

    # 공을 획득한 팀의 방향 전환
    reverse(got_ball_idx)

print(ans)