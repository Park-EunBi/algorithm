import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 시간 단축
# mn = min(b for bo in board for b in bo)
# mx = max(b for bo in board for b in bo)

ret = float('inf')
height = 0
# 높이를 h로 맞추었을 때의 시간 구하기
# for h in range(mn, mx + 1): # 시간 단축
for h in range(257):
    inven = b
    time = 0

    for i in range(n):
        for j in range(m):
            # 인벤에 넣기
            if board[i][j] > h:
                temp = board[i][j] - h
                inven += temp
                time += (temp * 2)

            # 인벤에서 꺼내기
            # elif board[i][j] < h:
            else: # 시간 단축
                temp = h - board[i][j]
                inven -= temp
                # if inven < 0: # 여기서 체크하면 틀림
                #     break
                time += temp

    if inven >= 0: # 등호 포함
        if ret >= time:
            height = h
            ret = time

print(ret, height)