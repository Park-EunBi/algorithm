# 사각형 회전
# - 인덱스 규칙을 파악하자

# [1] 정사각형
n = 5
board = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print('<<board - 정사각형 회전>>')
for b in board:
    print(*b)
print()

# 1. 90도 회전
temp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp[j][n - i - 1] = board[i][j]

print('<<90도 회전>>')
for t in temp:
    print(*t)
print()

# 2. 180도 회전
temp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp[n - i - 1][n - j - 1] = board[i][j]

print('<<180도 회전>>')
for t in temp:
    print(*t)
print()

# 3. 270도 회전
temp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        temp[n - 1 - j][i] = board[i][j]

print('<<270도 회전>>')
for t in temp:
    print(*t)
print()

##############
# [2] 직사각형
n, m = 3, 4
board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print('<<board - 직사각형 회전>>')
for b in board:
    print(*b)
print()

# 90도 회전
temp = [[0 for _ in range(m)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        temp[j][m-i-1] = board[i][j]

print('<<90도 회전>>')
for t in temp:
    print(*t)
print()

# 180도 회전
temp = [[0 for _ in range(m)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        temp[n-i-1][m-j-1] = board[i][j]

print('<<180도 회전>>')
for t in temp:
    print(*t)
print()

# 270도 회전
temp = [[0 for _ in range(m)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        temp[m-j-1][i] = board[i][j]

print('<<270도 회전>>')
for t in temp:
    print(*t)
print()