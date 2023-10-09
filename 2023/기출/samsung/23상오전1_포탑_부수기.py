from collections import deque

n, m, k = map(int, input().split())

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 언제 각성했는지 (?)
rec = [
    [0] * m
    for _ in range(n)
]

# 우, 하, 좌, 상
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dxs2, dys2 = [0, 0, 0, -1, -1, -1, 1, 1, 1], [0, -1, 1, 0, -1, 1, 0, -1, 1]

turn = 0

# 레이저 공격 방문 여무, 경로 방향 기록
vis = [
    [0] * m
    for _ in range(n)
]
# 레이져 공격시 최단경로 역추적시 사용
back_x = [
    [0] * m
    for _ in range(n)
]
back_y = [
    [0] * m
    for _ in range(n)
]

# 공격 무관 여부
is_active = [
    [False] * m
    for _ in range(n)
]

# 포탑 구조체 정의
class Turrent:
    def __init__(self, x, y, r, p):
        self.x = x # 포탑의 행
        self.y = y # 포탑의 열
        self.r = r # 포탑의 최근 공격 여부
        self.p = p # 포탑의 공격력

# 살아있는 포탑 관리
live_turret = []

# 턴 시작 전 전처리
def init():
    global turn

    turn += 1
    for i in range(n):
        for j in range(m):
            vis[i][j] = False # 레이저 방문 여부
            is_active[i][j] = False # 공격과 무관한지 확인

# 각성 - 가장 약한 포탑이 n + m 만큼 강해짐
def awake():
    # 우선순위에 맞도록 lambda로 한 번에 정렬
    live_turret.sort(key=lambda x : (x.p, -x.r, -(x.x + x.y), -x.y))

    # 가장 약한 포탑
    weak_turret = live_turret[0]
    x = weak_turret.x
    y = weak_turret.y

    board[x][y] += n + m # 공격력 증가
    rec[x][y] = turn # 몇번째 턴에 공격했는지
    # 각성한 포탑 정보 재설정
    weak_turret.p = board[x][y]
    weak_turret.r = rec[x][y]
    is_active[x][y] = True # 공격과 연관됨

    live_turret[0] = weak_turret


# 레이저 공격
def laser_attack():
    # 정렬된 포탑 중 가장 앞선 포탄 == 각성 포탑
    weak_turret = live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    # 정렬된 포탑 중 가장 튀 포탑이
    # 각성 포탑을 제외한 포탑 중 가장 강한 포탑
    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    # bfs를 통해 최댄 경로 관리
    q = deque()
    vis[sx][sy] = True
    q.append((sx, sy))

    # 가장 강한 포탑 도달 가능 여부 관리
    can_attack = False

    while q:
        x, y = q.popleft()
        # 바로 가장 강한 포탑에 도닥할 수 있다면 break
        if x == ex and y == ey:
            can_attack = True
            break

        # 우하좌상 방문
        for dx, dy in zip(dxs, dys):
            # 범위 넘어서면 앞으로 돌아가기에 % 연산
            nx = (x + dx + n) % n
            ny = (y + dy + m) % m

            # 이미 방문하면 continue
            if vis[nx][ny]:
                continue

            # 벽이라면 continue
            if board[nx][ny] == 0:
                continue

            vis[nx][ny] = True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            q.append((nx, ny))

    # 도달 가능하면 공격
    if can_attack:
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        is_active[ex][ey] = True

        # 기존 경로 역추적하며 절반 공격
        cx = back_x[ex][ey]
        cy = back_y[ex][ey]

        while not (cx == sx and cy == sy):
            board[cx][cy] -= power // 2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            is_active[cx][cy] = True

            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]

            cx = next_cx
            cy = next_cy

    # 공격 성공 여부 반환
    return can_attack

# 포탄 공격
def bomb_attack():
    weak_turret = live_turret[0]
    sx = weak_turret.x
    sy = weak_turret.y
    power = weak_turret.p

    strong_turret = live_turret[-1]
    ex = strong_turret.x
    ey = strong_turret.y

    # 가장 강한 포탑의 3*3 범위를 탐색하며
    # 각각 공격
    for dx2, dy2 in zip(dxs2, dys2):
        nx = (ex + dx2 + n) % n
        ny = (ey + dy2 + m) % m

        # 자기 자신일 경우 pass
        if nx == sx and ny == sy:
            continue

        # 가장 강한 포탄일 경우 pow 만큼 공격
        if nx == ex and ny == ey:
            board[nx][ny] -= power
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True

        else:
            board[nx][ny] -= power // 2
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True

# 공격에 관여하지 않은 경우 += 1
def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]:
                continue
            if board[i][j] == 0:
                continue
            board[i][j] += 1

# k 번 진행
for _ in range(k):
    # 살아있는 포탑 정리
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turret = Turrent(i, j, rec[i][j], board[i][j])
                live_turret.append(new_turret)

    # 살아있는 포탑이 1개 이하라면 바로 종료
    if len(live_turret) <= 1:
        break

    # 턴 전 전처리
    init()

    # 각성
    awake()

    # 레이져 공격
    is_suc = laser_attack()
    # 포탄 공격
    if not is_suc:
        bomb_attack()

    # 공격에 관여하지 않았다면 += 1
    reserve()

# 살아있는 포탑 중 가장 큰 값
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])

print(ans)
