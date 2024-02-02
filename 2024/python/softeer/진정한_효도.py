import sys
board = [
    list(map(int, input().split()))
    for _ in range(3)
]

ret = 99
# 가로
for i in range(3):
    make_one = abs(1 - board[i][0]) + abs(1 - board[i][1]) + abs(1 - board[i][2])
    make_two = abs(2 - board[i][0]) + abs(2 - board[i][1]) + abs(2 - board[i][2])
    make_three = abs(3 - board[i][0]) + abs(3 - board[i][1]) + abs(3 - board[i][2])
    ret = min(make_one, make_two, make_three, ret)

# 세로
for i in range(3):
    make_one = abs(1 - board[0][i]) + abs(1 - board[1][i]) + abs(1 - board[2][i])
    make_two = abs(2 - board[0][i]) + abs(2 - board[1][i]) + abs(2 - board[2][i])
    make_three = abs(3 - board[0][i]) + abs(3 - board[1][i]) + abs(3 - board[2][i])
    ret = min(make_one, make_two, make_three, ret)

print(ret)