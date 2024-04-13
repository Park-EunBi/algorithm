n = 5
board = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print('<<init board>>')
for b in board:
    print(*b)
print()

temp = [arr[:] for arr in board]

# (1, 1) ~ (3, 3) 90도 회전
sx, sy = 1, 1
square_size = 3
for x in range(sx, sx + square_size):
    for y in range(sy, sy + square_size):
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
        ox, oy = x - sx, y - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        temp[rx + sx][ry + sy] = board[x][y]

print('<<after>>')
for b in temp:
    print(*b)
