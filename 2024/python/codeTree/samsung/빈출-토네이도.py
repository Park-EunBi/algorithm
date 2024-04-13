def to_in_tornado(n):
    if n == 1:
        return [[1]]

    ans = [[0 for _ in range(n)] for _ in range(n)]

    x, y, d_idx = 0, 0, 0

    for i in range(n * n):
        ans[x][y] = i + 1
        if d_idx == 0:
            y += 1
            if y == n - 1 or ans[x][y + 1] != 0:
                d_idx = 1
        elif d_idx == 1:
            x += 1
            if x == n - 1 or ans[x + 1][y] != 0:
                d_idx = 2
        elif d_idx == 2:
            y -= 1
            if y == 0 or ans[x][y - 1] != 0:
                d_idx = 3
        elif d_idx == 3:
            x -= 1
            if x == n - 1 or ans[x - 1][y] != 0:
                d_idx = 0

    return ans

arr = [[0 for _ in range(5)] for _ in range(5)]
def to_out_tornado(n):
    global arr
    # d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x = len(arr)//2
    y = len(arr)//2
    num = 0 # 채워 넣을 값
    dist = 1
    d_idx = 0
    move_cnt = 0

    while 1:
        for _ in range(dist):
            dy, dx = d[d_idx]
            nx = x + dx
            ny = y + dy
            if (x, y) == (-1, 0):
                return
            num += 1
            arr[nx][ny] = num
            x = nx
            y = ny
        move_cnt += 1
        d_idx = (d_idx + 1) % 4
        if move_cnt == 2:
            dist += 1
            move_cnt = 0

print('<<안에서 밖으로>>')
to_out_tornado(5)
for a in arr:
    print(*a)
print()

print('<<밖에서 안으로>>')
arr = to_in_tornado(5)
for a in arr:
    print(*a)