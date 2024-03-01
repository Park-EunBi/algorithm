# 0: 빈 공간, 1: /, 2: \
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = -float('inf')
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상

# /
one_dir = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}

# \
two_dir = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def move(x, y, d):
    # /
    if board[x][y] == 1:
        d = one_dir[d]
    # \
    elif board[x][y] == 2:
        d = two_dir[d]

    nx, ny = x + dxs[d], y + dys[d] # 변경 한 값으로 if else 를 돌리는 거 x
    return nx, ny, d

def simulation(x, y, d):
    global ans
    time = 1

    while in_range(x, y):
        x, y, d = move(x, y, d)
        time += 1

    return time


# 시작 지점 설정 1. - 행 (i: 0, n-1)
for j in range(n):
    ans = max(ans, simulation(0, j, 1))
    ans = max(ans, simulation(n-1, j, 3))

# 시작 지점 설정 2. - 열 (j: 0, n-1)
for i in range(n):
    ans = max(ans, simulation(i, 0, 0))
    ans = max(ans, simulation(i, n - 1, 2))

print(ans)

'''
3
0 1 1 
0 0 0 
2 2 1

8

# 방문처리 하지 않아도 된다. <- 빠져나가지 못할까봐 생성한건데 그런 경우 없음 
# 방문했던 곳 다시 방문할 수 있는데 visited 배열 때문에 오류 남 
'''

'''
# sol_2
# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def calc(x, y, move_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
	# 1번 블럭에서는 방향이 다음과 같이 변합니다 : 0<->3 1<->2
	# 2번 블럭에서는 방향이 다음과 같이 변합니다 : 0<->2 1<->3
    
    elapsed_time = 1
    
    while in_range(x, y):
        if grid[x][y] == 1:
            move_dir = 3 - move_dir
        elif grid[x][y] == 2:
            move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        
        x, y = x + dxs[move_dir], y + dys[move_dir]
        elapsed_time += 1
    
    return elapsed_time


# 각각의 상하좌우 방향에 대해
# 가능한 모든 위치에서 걸리는 시간을 계산한 후,
# 그 중 최댓값을 구합니다.
ans = 0
for i in range(n):
    ans = max(ans, calc(n - 1, i, 0))
    ans = max(ans, calc(0, i, 1))
    ans = max(ans, calc(i, n - 1, 2))
    ans = max(ans, calc(i, 0, 3))
	
print(ans)
'''