# sol_1 - https://sinawi.tistory.com/241
matrix = [input() for _ in range(5)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result_set = set()

def backtrack(arr, index=0, S=0, Y=0):
    tmp = arr
    if Y > 3:
        return
    if index == 6:
        arr.sort()
        result_set.add(tuple(arr))
    else:
        adjacents = []
        for node in range(len(arr)):
            for i in range(4):
                dx = arr[node][0] + delta[i][0]
                dy = arr[node][1] + delta[i][1]
                if 0 > dx or 5 <= dx or 0 > dy or 5 <= dy: continue
                if (dx, dy) in arr: continue
                adjacents.append((dx,dy))
        for adjacent in adjacents:
            nx = adjacent[0]
            ny = adjacent[1]
            if matrix[nx][ny] == 'S':
                backtrack(arr+[(nx,ny)], index+1, S+1, Y)
            else:
                backtrack(arr+[(nx,ny)], index+1, S, Y+1)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'S':
            backtrack([(i, j)], index=0, S=1)

print(len(result_set))

# sol_2 - https://www.youtube.com/watch?v=DWdFSOehwFI
# from collections import deque
# def bfs(si,sj):
#     q = deque()
#     vv = [[0]*5 for _ in range(5)]
#
#     q.append((si,sj))
#     vv[si][sj]=1
#     cnt = 1
#
#     while q:
#         ci,cj = q.popleft()
#         for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni,nj = ci+di, cj+dj
#             if 0<=ni<5 and 0<=nj<5 and vv[ni][nj]==0 and v[ni][nj]==1:
#                 q.append((ni,nj))
#                 vv[ni][nj]=1
#                 cnt+=1
#     return cnt==7
#
# def check():
#     for i in range(5):
#         for j in range(5):
#             if v[i][j]==1:
#                 return bfs(i,j)
#
# def dfs(n, cnt, scnt):
#     global ans
#     if cnt>7:                   # 가지치기: 이미 7명을 넘었으면 7공주 불가!
#         return
#
#     if n == 25:
#         if cnt==7 and scnt>=4:  # 7명 그룹이고, 4명이상이 다솜파인 경우
#             if check():         # 인접했는지 체크해서 모두 인접시 정답+=1
#                 ans+=1
#         return
#
#     v[n//5][n%5]=1              # 포함하는 경우 표시
#     dfs(n+1, cnt+1, scnt+int(arr[n//5][n%5]=='S'))
#     v[n//5][n%5]=0              # 원상복구
#     dfs(n+1, cnt, scnt)         # 포함하지 않는 경우
#
# arr = [input() for _ in range(5)]
# ans = 0
# v = [[0]*5 for _ in range(5)]
# # 학생번호(0~24), 포함학생수, 다솜파학생수
# dfs(0, 0, 0)
# print(ans)

# sol3 - 내 풀이
# # Y(0): 임도연, S(1): 이다솜
# from collections import deque
# board = [input() for _ in range(5)]
#
# dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
#
# def in_range(x, y):
#     if x < 0 or x >= 5 or y < 0 or y >= 5:
#         return False
#     return True
#
# # main
# dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
# # ret = set()
# ret = []
# choose = []
# ans = 0
# visited = [[0 for _ in range(5)] for _ in range(5)]
# def choice(x, y, num):
#     global ans, visited
#     if num == 6:
#         visited = [[0 for _ in range(5)] for _ in range(5)]
#         # 임도연파 수 세기
#         # print(choose)
#         # ret.add(''.join(choose))
#         print(''.join(choose))
#         ret.append(''.join(choose))
#         ans += 1
#         return
#
#     for dx, dy in zip(dxs, dys):
#         nx, ny = x + dx, y + dy
#         # print(nx, ny)
#         if in_range(nx,ny) and not visited[nx][ny]:
#             visited[nx][ny] = 1
#             choose.append(board[nx][ny])
#             choice(nx, ny, num + 1)
#             choose.pop()
#
# # choose.append(board[1][1])
# # choice(1, 1, 0)
# # choose = []
# # choose.append(board[2][1])
# # choice(2, 1, 0)
#
#
# def calc():
#     ans = 0
#     for re in ret:
#         cnt = 0 # 임도연파 개수
#         for r in re:
#             # print(re)
#             if r == 'Y':
#                 cnt += 1
#             if cnt > 4:
#                 break
#         if cnt <= 3:
#             ans += 1
#     return ans
#
#
# # main
# # 백트래킹으로 모든 경우 탐방
# for i in range(5):
#     for j in range(5):
#         # 시작점 설정
#         choose = []
#         choose.append(board[i][j])
#         choice(i, j, 0)
#
# ret = set(ret)
# print(ret)
#
# # 조건 확인
# ans = calc()
# print(ans)
#
#
# print('<<board>>')
# for b in board:
#     print(*b)
# print()