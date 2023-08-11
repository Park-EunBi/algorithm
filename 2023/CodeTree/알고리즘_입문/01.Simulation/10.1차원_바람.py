# https://www.codetree.ai/missions/2/problems/The-1D-wind-blows?utm_source=clipboard&utm_medium=text
# q 번의 바람, 틀정 행의 모든 원소들을 왼, 오른쪽으로 한 칸씩 민다
# 위 아래로도 바람이 전파된다 (조건: 하나라도 같은 열에 같은 숫자 있는 경우 행이 밀렸던 방향과 반대로)
# q 개의 바람을 거친 후 건물의 상태 출력
SHIFT_RIGHT = 0
SHIFT_LEFT = 1

n, m, q = map(int, input().split())

a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


# 행, 방향

# 위 방향 전파를 먼저 처리하고, 아래 전파를 처리하면 된다

# row의 원소를 밀기
# dir == 0: 오른쪽, 1: 왼쪽
def shift(row, curr_dir):
    # 오른쪽으로 밀어야 하는 경우
    if curr_dir == SHIFT_RIGHT:
        a[row].insert(1, a[row].pop())
    else:
        a[row].insert(m, a[row].pop(1))


# 같은 열에 같은 숫자가 있는지 판단
def has_same_number(row1, row2):
    return any([
        a[row1][col] == a[row2][col]
        for col in range(1, m + 1)
    ])


# 반대 방향의 값을 반환
def flip(curr_dir):
    return SHIFT_RIGHT if curr_dir == SHIFT_LEFT else SHIFT_LEFT


# 움직이기
def simulate(start_row, start_dir):
    # step1. 바람이 처음으로 불어온 행들을 밀어주기
    shift(start_row, start_dir)

    # 방향 반전
    start_dir = flip(start_dir)

    # step2. 위 방향 전파
    curr_dir = start_dir
    for row in range(start_row, 1, -1):
        # 인접한 행끼리 같은 숫자를 가지면 한 칸 shift 하고
        # "방향을 반대"로 바꿔서 전파 - 틀린 이유 1
        if has_same_number(row, row - 1):
            shift(row - 1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break

    # step3. 아래 방향 전파
    curr_dir = start_dir
    for row in range(start_row, n):
        if has_same_number(row, row + 1):
            shift(row + 1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break


for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start=1):
        a[row][col] = num

for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)

    # 조건에 맞춰 움직여봅니다
    simulate(r, SHIFT_RIGHT if d == 'L' else SHIFT_LEFT)

# 출력
for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end=" ")
    print()

'''
# 도전...
def right_wind(x):
    x -= 1
    tmp = maps[x][-1]
    for i in range(m-1, 0, -1):
        maps[x][i] = maps[x][i - 1]
    maps[x][0] = tmp

def left_wind(x):
    x -= 1
    tmp = maps[x][0]
    for i in range(m -1):
        maps[x][i] = maps[x][i + 1]
    maps[x][-1] = tmp

def check_col_up(x):
    # x -= 1
    for i in range(m):
        if maps[x-1][i] == maps[x][i]:
            return True
    return False

def check_col_down(x):
    x -= 1
    for i in range(m):
        if maps[x + 1][i] == maps[x][i]:
            return True
    return False

def next_wind_up(x):
    print(maps)
    x -= 1
    # up = x - 2
    if x - 1 < 0:
        return 
    # 같은 열 판단 
    if check_col_up(x):
        if d == 'L':
            right_wind(x - 1)
        else:
            left_wind(x - 1)
        next_wind_up(x - 1)
    return 


def next_wind_down(x):
    x -= 1
    # down = x + 2
    if x + 1 >= n:
        return 
    if check_col_down(x):
        if d == 'L':
            right_wind(x - 1)
        else:
            left_wind(x - 1)
        next_wind_down(x - 1)
    return 

for _ in range(q):
    if d == 'L':
        left_wind(r)

    else: 
        right_wind(r)
    next_wind_up(r)
    print(maps)
    next_wind_down(r)

for m in maps:
    print(*m)
'''