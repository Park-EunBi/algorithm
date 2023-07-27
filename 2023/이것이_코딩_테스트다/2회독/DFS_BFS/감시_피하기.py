# 상하좌우로 감시, 장애물 뒤편에 있는 학생은 볼 수 없음
# T: 선생님, S: 학생, O: 장애물
# 3개의 감시물을 설치하여 모든 학생이 감시를 피할 수 있는 방법 출력
# 모든 조합을 찾으면 된다 (DFS, BFS 사용)

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = [] # 빈공간 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append(((i, j)))
        # 장애물 설치 가능 공간 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

    # 감시 진행
    def watch(x, y, direction):
        if direction == 0:
            while y>= 0:
                if board[x][y] == 'S': # 학생이 있는 경우
                    return True
                if board[x][y] == 'O': # 장애물이 있는 경우
                    return False
                y -= 1

        if direction == 1:
            while y < n:
                if board[x][y] == 'S': # 학생이 있는 경우
                    return True
                if board[x][y] == 'O': # 장애물이 있는 경우
                    return False
                y += 1

        if direction == 2:
            while x >= 0:
                if board[x][y] == 'S': # 학생이 있는 경우
                    return True
                if board[x][y] == 'O': # 장애물이 있는 경우
                    return False
                x -= 1

        if direction == 3:
            while x < n:
                if board[x][y] == 'S': # 학생이 있는 경우
                    return True
                if board[x][y] == 'O': # 장애물이 있는 경우
                    return False
                x += 1
        return False

    # 장애물 설치 이후 학생 감지 확인
    def process():
        for x, y in teachers:
            for i in range(4):
                if watch(x, y, i):
                    return True
        return False

find = False # 한 명이라도 감지되지 않도록 설치할 수 있는지

# 빈 공간에서 3개를 뽑는 모든 조합
for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        board[x][y] = 'O'
    # 한 명도 감지되지 않는 경우
    if not process():
        find = True
        break
    # 설치된 장애물 제거
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')

'''
<testCase1>
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

<answer1>
YES

<testCase2>
4
S S S T
X X X X
X X X X
T T T X

<answer2>
NO
'''