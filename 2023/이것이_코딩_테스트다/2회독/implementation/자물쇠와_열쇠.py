def rotate(key):
    # 회전 알고리즘 (90도 회전)
    n = len(key)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n - 1 - i] = key[i][j]

    return ret


def check(startX, startY, key, lock, board_size, start, end):
    # board 생성
    board = [[0] * board_size for _ in range(board_size)]

    # board에 key 넣기
    for i in range(len(key)):
        for j in range(len(key)):
            board[startX + i][startY + j] += key[i][j]

    # key가 들어간 board에 lock 넣기 (더하기)
    for i in range(start, end):
        for j in range(start, end):
            board[i][j] += lock[i - start][j - start]
            # 모든 lock이 1이어야만 잠금 풀림
            if board[i][j] != 1:
                return False
    else:
        return True


def solution(key, lock):
    start = len(key) - 1  # board에서 lock의 시작 위치
    end = start + len(lock)  # board에서 lock의 종료 위치
    board_size = len(lock) + start * 2

    # 1. board 생성
    # 2. check (move, rotate)

    # 4방향 회전
    for rotation in range(4):
        # key 회전
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, board_size, start, end):
                    return True
        key = rotate(key)

    return False