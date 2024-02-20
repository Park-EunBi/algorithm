from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
q = deque()

ans = 0
append_list = []  # 값 바꾸기 위해 좌표 등록
total = 0  # 분리한 판의 계란 수
cnt = 0  # 분리한 판 수

def canGo(x, y):
    # 1. 범위 확인
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
        # 이동 확인, 방문 확인
    if visited[x][y]:
        return False
    return True

def push(x, y):
    global total, cnt
    # 1. 추가
    q.append((x, y))
    # 2. 방문 처리
    visited[x][y] = 1
    # 3. 계산 데이터 등록
    total += board[x][y]
    cnt += 1
    append_list.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if canGo(nx, ny) and (l <= abs(board[nx][ny] - board[x][y]) <= r):
                push(nx, ny)

    change = total // cnt
    for x, y in append_list:
        board[x][y] = change

while 1:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if canGo(i, j):
                # 값 추가
                push(i, j)
                visited[i][j] = 1
                bfs()
                count += 1

                # 초기화
                append_list = []  # 값 바꾸기 위해 좌표 등록
                total = 0  # 분리한 판의 계란 수
                cnt = 0  # 분리한 판 수

    if count == n * n:
        print(ans)
        break

    ans += 1

'''
# sol_2
from collections import deque

# 변수 선언 및 입력
n, L, R = tuple(map(int, input().split()))

egg = [
    list(map(int, input().split()))
    for _ in range(n)
]

bfs_q = deque()
egg_group = []
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, curr_egg):
    if not in_range(x, y):
        return False

    egg_diff = abs(egg[x][y] - curr_egg)
    return not visited[x][y] \
           and L <= egg_diff and egg_diff <= R


# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            # L, R 사이인 경우에만 합쳐질 수 있습니다.
            if can_go(new_x, new_y, egg[curr_x][curr_y]):
                bfs_q.append((new_x, new_y))
                egg_group.append((new_x, new_y))
                visited[new_x][new_y] = True


# 계란들을 합칩니다.
def merge_eggs():
    sum_of_eggs = sum([
        egg[x][y]
        for x, y in egg_group
    ])

    for x, y in egg_group:
        egg[x][y] = sum_of_eggs // len(egg_group)


# 조건에 맞게 계란의 양을 바꿔줍니다.
def move_eggs():
    global egg_group

    # BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()

    is_changed = False

    # 아직 방문하지 못한 칸에 대해
    # BFS 탐색을 통해 합쳐질 계란들을 찾아냅니다.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 합쳐질 계란 목록을 담을 곳을 초기화합니다.
                egg_group = []

                bfs_q.append((i, j))
                egg_group.append((i, j))
                visited[i][j] = True

                bfs()

                # 계란의 이동이 한번이라도 일어났는지를 확인합니다.
                if len(egg_group) > 1:
                    is_changed = True

                # (i, j)와 관련이 있는 계란들을 합칩니다.
                merge_eggs()

    return is_changed


move_cnt = 0

# 이동이 더 이상 필요 없을 때까지
# 계란의 이동을 반복합니다.
while True:
    is_changed = move_eggs()
    if not is_changed:
        break

    move_cnt += 1

print(move_cnt)
'''