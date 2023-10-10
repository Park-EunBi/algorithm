EMPTY = (-1, -1, -1, -1, -1, -1)

# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))

# 총 목록 관리
gun = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        # 총이 놓여 있는 칸
        if nums[j] != 0:
            gun[i][j].append(nums[j])

# (num, x, y, d, s, a)
# num: 플레이어 번호, d: 방향, s: 초기 능력치, a: 총의 공격력 (default:0)
player = []
for i in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    player.append((i, x - 1, y - 1, d, s, 0))


# ↑, →, ↓, ←
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

points = [0] * m

# 격자 범위 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 다음 위치와 방향 찾기
def get_next(x, y, d):
    nx, ny = x + dxs[d], y + dys[d]
    # 격자 넘어서면 방향 뒤집기
    if not in_range(nx, ny):
        d = (d + 2) if d < 2 else (d - 2)
        nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny, d)

# player 가 있는지 확인
def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = player[i]
        if pos == (x, y):
            return player[i]
    return EMPTY

# player p의 정보 갱신
def update(p):
    num, _, _, _, _, _ = p
    # player 위치 찾아 값 갱신
    for i in range(m):
        num_i, _, _, _, _, _ = player[i]

        if num_i == num:
            player[i] = p
            break

# 플레이어 p를 pos 위치로 이동
def move(p, pos):
    num, x, y, d, s, a = p # 현재 상태
    nx, ny = pos # 이동시킬 위치

    # 가장 좋은 총으로 갱신
    gun[nx][ny].append(a) # 총 버리기
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)

# 진 사람
def loser_move(p):
    num, x, y, d, s, a = p
    # 총 내려놓기
    gun[x][y].append(a)

    # 빈 공간으로 이동
    for i in range(4):
        ndir = (d + i) % 4
        nx, ny = x + dxs[ndir], y + dys[ndir]
        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx, ny))
            break

# 결투
def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    # (초기 능력치 + 총의 공격력) vs (초기 능력치)

    # p1 이김
    if (s1 + a1, s1) > (s2 + a2, s2):
        points[num1] += (s1 + a1) - (s2 + a2)
        loser_move(p2)
        move(p1, pos)
    # p2 이김
    else:
        points[num2] += (s2 + a2) - (s1 + a1)
        loser_move(p1)
        move(p2, pos)

def simulation():
    for i in range(m):
        num, x, y, d, s, a = player[i]

        # step 1-1. 움직일 위치와 방향 구하기
        nx, ny, ndir = get_next(x, y, d)

        # 해당 위치에 있는 전 플레이어 정보
        next_player = find_player((nx, ny))

        # 현재 플레이어 위치, 방향 보정
        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        # step2. 해당 위치로 이동
        # step2-1. 플레이어가 없다면 이동
        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        # step2-2. 플레이어가 있다면 결투
        else: duel(curr_player, next_player, (nx, ny))

for _ in range(k):
    simulation()

print(*points)