N, M, P, C, D = map(int, input().split())
v = [[0]*N for _ in range(N)]

ri, rj = map(lambda x:int(x)-1, input().split())
v[ri][rj]=-1                                # 루돌프표시(-1)

score = [0]*(P+1)
alive = [1]*(P+1)
alive[0] = 0                                # 첫 번째는 없는 산타
wakeup_turn = [1]*(P+1)

santa = [[N]*2 for _ in range(P+1)]         # 빈 자리, 번호 맞추기
for _ in range(1, P + 1):
    n,i,j = map(int, input().split())
    santa[n]=[i-1,j-1]                      # i, j
    v[i-1][j-1] = n

def move_santa(cur,si,sj,di,dj,mul):
    q = [(cur,si,sj,mul)]           # cur번 산타를 si,sj에서 di,dj방향으로 mul칸 이동

    while q:
        cur,ci,cj,mul=q.pop(0)
        # 진행방향 mul칸만큼 이동시켜서 범위내이고 산타있으면 q삽입/범위밖 처리
        ni,nj=ci+di*mul, cj+dj*mul
        if 0<=ni<N and 0<=nj<N:     # 범위내 => 산타 O, X
            if v[ni][nj]==0:        # 빈 칸 => 이동처리
                v[ni][nj]=cur
                santa[cur]=[ni,nj]
                return
            else:                   # 산타 O => 연쇄이동
                q.append((v[ni][nj],ni,nj,1))   # 한칸 이동, v[ni][nj]: 다음 산타번호
                v[ni][nj]=cur
                santa[cur]=[ni,nj]
        else:                       # 범위밖 => 탈락 => 끝
            alive[cur]=0
            return

for turn in range(1, M+1):
    # [0] 모두 탈락 시(alive 모두 0) => break
    if alive.count(1)==0:
        break

    # [1-1] 루돌프 이동: 가장 가까운 산타찾기
    mn = 2*N**2
    for idx in range(1, P+1):
        if alive[idx]==0:   continue    # 타락한 산타 => skip..

        si,sj=santa[idx]
        dist=(ri-si)**2+(rj-sj)**2      # 현재거리
        if mn>dist:
            mn=dist
            mlst=[(si,sj,idx)]          # 최소거리=>새리스트
        elif mn==dist:                  # 같은최소=>추가
            mlst.append((si,sj,idx))
    mlst.sort(reverse=True)             # 행 큰>열 큰
    si,sj,mn_idx = mlst[0]              # 돌격 목표산타!

    # [1-2] 대상 산타 방향으로 루돌프 이동
    rdi = rdj = 0
    if ri>si:   rdi=-1  # 산타가 좌표 작은값 => -1방향 이동
    elif ri<si: rdi=1

    if rj>sj:   rdj=-1
    elif rj<sj: rdj=1

    v[ri][rj]=0             # 루돌프 현재자리 지우기
    ri,rj = ri+rdi, rj+rdj  # 루돌프 이동
    v[ri][rj]=-1            # 이동한 자리에 표시

    # [1-3] 루돌프와 산타가 충돌한 경우 산타 밀리는 처리
    if (ri,rj)==(si,sj):            # 충돌!
        score[mn_idx]+=C            # 산타는 C점 획득
        wakeup_turn[mn_idx]=turn+2  # 깨어날 턴 번호를 저장
        move_santa(mn_idx,si,sj,rdi,rdj,C)  # 산타 C칸이동

    # [2-1] 순서대로 산타이동: 기절하지 않은 경우(산타의 턴 <= turn)
    for idx in range(1, P+1):
        if alive[idx]==0:           continue    # 탈락한 경우 skip
        if wakeup_turn[idx]>turn:   continue    # 깨어날 턴이 아직 안된경우

        si,sj = santa[idx]
        mn_dist = (ri-si)**2 + (rj-sj)**2
        tlst = []
        # 상우하좌 순으로 최소거리 찾기
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj=si+di,sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            # 범위내, 산타 없고(<=0),더 짧은 거리인 경우
            if 0<=ni<N and 0<=nj<N and v[ni][nj]<=0 and mn_dist>dist:
                mn_dist = dist
                tlst.append((ni,nj,di,dj))
        if len(tlst)==0:    continue    # 이동할 위치 없음
        ni,nj,di,dj = tlst[-1]          # 마지막에 추가된(더 짧은 거리)

        # [2-2] 루돌프와 충돌시 처리
        if (ri,rj)==(ni,nj):            # 루돌프와 충돌: 반대로 튕겨나감!
            score[idx]+=D
            wakeup_turn[idx]=turn+2
            v[si][sj]=0
            move_santa(idx,ni,nj,-di,-dj,D)
        else:                           # 빈 칸: 좌표갱신, 이동처리
            v[si][sj]=0
            v[ni][nj]=idx
            santa[idx]=[ni,nj]

    # [3] 점수획득: alive 산타는 +1점
    for i in range(1,P+1):
        if alive[i]==1:
            score[i]+=1

print(*score[1:])
#
# santa = [[0, 0] for _ in range(p)] # 점수, 기절 종료 시간
# santa.insert(0, [])
#
# dxs, dys = [-1, 0, 1, 0, -1, 1, 1, -1], [0, 1, 0, -1, 1, 1, -1, -1]
#
# print('<<inital - board>>')
# for b in board:
#     print(*b)
# print()
# print('<<inital - santa>>')
# for i in range(1, p + 1):
#     print(santa[i], end=' ')
# print()
# print('--------start--------')
#
# def in_range(x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#     return True
#
# # 충돌 난 위치, 돌진한 산타 번호
# def next_santa(x, y, collision_santa, d):
#
#     # 밀려날 방향 확인
#     nx, ny = x + d[0], y + d[1]
#     print(f'{x, y}, {nx, ny}, collision: {collision_santa}, d: {d}')
#     # 밀려 났는데 범위 안이면
#     if in_range(nx, ny):
#         # 거기에 또 산다가 없다면
#         if board[nx][ny] <= 0:
#             # 이동 후 돌진 산타 기록
#             board[nx][ny] = board[x][y]
#             board[x][y] = collision_santa
#
#             print('<< 상호 작용 했는데 산타가 없음 >>')
#             for b in board:
#                 print(*b)
#             print()
#             return
#         # 산타가 있다면 - 재귀
#         else:
#             # 일단 돌진한 산타 두고
#             # board[x][y] = collision_santa
#             # 재귀
#             print(f'재귀: {nx, ny}, 번호: {board[x][y]}, d: {d}')
#             next_santa(nx, ny, board[x][y], d)
#             board[x][y] = 0
#
#     # 밀려 났는데 밖이면 돌진한 산타 위치만 등록
#     else:
#         board[x][y] = collision_santa
#         print('<< 상호 작용 했는데 범위 벗어남 >>')
#         for b in board:
#             print(*b)
#         print()
#         # return
#
#
# # 충돌 처리
# def collision(cur, sx, sy, dx, dy, mul): # 산타 번호, 시작 위치, 이동 방향, 이동 칸 수
#     print('collision')
#     print(f'{cur}번 산타가 ({sx, sy})에서 ({dx, dy}) 방향으로 {mul}칸 이동')
#     q = [(cur, sx, sy, mul)]
#
#     while q:
#         cur, sx, sy, mul = q.pop(0)
#         nx, ny = sx + (dx * mul), sy + (dy * mul)
#         print(nx, ny)
#         if in_range(nx, ny):
#             # 빈 칸 이면
#             if board[nx][ny] == 0:
#                 print('here')
#                 board[nx][ny] = cur
#                 for b in board:
#                     print(*b)
#                 return board
#             # 다른 산타 있으면
#             else:
#                 q.append((board[nx][ny], nx, ny, 1))
#                 santa[board[nx][ny]][0] += d # 점수 추가
#                 board[nx][ny] = cur
#         # 범위를 벗어났다면
#         # else:
#
#
#
#
#
#
#
# # def collsion(move_x, move_y, sitting_x, sitting_y, d, score):
# #     # move_x, y는 sitting_x, y를 d 방향으로 밀어냄
# #     # socre 는 s, d 점수 중 어느 것을 사용할지
# #
# #     # 1. sitting_x, y는 d 방향으로 score 칸 만큼 이동
# #     print(f'크기: {score}')
# #     print(f'밀리기 전 위치: {sitting_x, sitting_y}, 밀려난 방향: ', d)
# #     n_x, n_y = move_x + (d[0] * score), move_y + (d[1] * score)
# #     print('밀려난 좌표: ', n_x, n_y)
# #
# #     # 2. 상호작용 처리
# #     if in_range(n_x, n_y):
# #         # 이동한 위치에 산타가 있다면
# #         if board[n_x][n_y] > 0:
# #             # 상호작용 발생생
# #             print('!!상호작용 발생!!')
# #             next_santa(n_x, n_y, board[sitting_x][sitting_y], d)
# #             # # 루돌프 이동
# #             # board[rx][ry] = 0
# #             # board[move_x][move_y] = -1
# #
# #         # 이동한 위치에 산타가 없다면
# #         else:
# #             # 루돌프 이동
# #             board[rx][ry] = 0
# #             board[move_x][move_y] = -1
# #             # 산타 이동
# #             board[n_x][n_y] = board[sitting_x][sitting_y]
# #             board[sitting_x][sitting_y] = 0
# #
# #     print('<<board - 충돌 이후>>')
# #     for b in board:
# #         print(*b)
# #     print()
#
#
#
#
#     # 2. 연쇄 작용
#
#
# def move_ru(time):
#     global rx, ry
#     # 1. 가장 가까운 산타 선택 - 탈락하지 않고, x -> y 큰 순으로
#     san_loc = [] # (x, y, dist)
#     for i in range(n):
#         for j in range(n):
#             # 산타면
#             if board[i][j] > 0:
#                 # 거리 계산
#                 dist = (i - rx) ** 2 + (j - ry) ** 2
#                 san_loc.append((i, j, dist))
#     san_loc.sort(reverse = True, key= lambda x: (-x[2], x[0], x[1]))
#
#     # 선택한 산타의 좌표
#     gx, gy = san_loc[0][0], san_loc[0][1]
#     print(f'선택한 산타의 좌표: {gx, gy}')
#
#     # print('<<move_ru - 가장 가까운 산타 찾기>>')
#     # print(san_loc)
#     # print()
#
#     # 2. 루돌프는 해당 산타 가장 인접한 방향으로 돌진 (8방향)
#     min_dist = float('inf')
#     min_nx, min_ny = -1, -1
#     d = -1
#     for dx, dy in zip(dxs, dys):
#         nx, ny = rx + dx, ry + dy
#         if in_range(nx, ny):
#             temp = abs(nx - gx) + abs(ny - gy)
#             print(f'nx : {nx}, ny: {ny}, temp: {temp}')
#             if temp < min_dist:
#                 min_nx, min_ny = nx, ny
#                 min_dist = temp
#                 d = (dx, dy)
#
#     print(min_nx, min_ny, d)
#
#     # 루돌프 이동
#     # rx, ry = min_nx, min_ny
#
#     # 충돌 확인
#     for santa_x, santa_y, _ in san_loc:
#         # print(rx, ry, santa_x, santa_y)
#         if (min_nx, min_ny) == (santa_x, santa_y):
#             # collsion(rx, ry, santa_x, santa_y, d, c)
#             collision(board[santa_x][santa_y], santa_x, santa_y, d[0], d[1], c)
#             santa[board[santa_x][santa_y]][0] += c # 산타 점수
#             santa[board[santa_x][santa_y]][1] = time + 1# 산타 기절
#
#             board[rx][ry] = 0
#             rx, ry = min_nx, min_ny
#             board[rx][ry] = -1
#
#     # 충돌하지 않았다면
#     # else:
#     #     # 루돌프 이동
#     #     board[rx][ry] = 0
#     #     rx, ry = min_nx, min_ny
#     #     board[rx][ry] = -1
#
#     print('<<board - after move_ru()>>')
#     for b in board:
#         print(*b)
#     print()
#
# def move_santa(time):
#     global board
#     temp_board = [[0 for _ in range(n)] for _ in range(n)]
#     temp_board[rx][ry] = - 1
#     temp_loc = []
#
#     santa_loc = [
#         (i, j, board[i][j], ) # 위치, 산타 번호
#         for i in range(n)
#         for j in range(n)
#         if board[i][j] > 0
#     ]
#     print(f'santa_loc: {santa_loc}')
#
#     for x, y, idx in santa_loc:
#         dist = (rx - x) ** 2 + (ry - y) ** 2
#         print(rx, ry, x, y, dist)
#
#         # 기절 산타 확인
#         if santa[idx][0] > time:
#             # 기절해있음 - 기절 위치 등록
#             temp_board[x][y] = idx
#             continue
#         # 기절 안 한 산타라면
#         else:
#             # 루돌프에게 가장 가까워지는 방향으로 이동
#             # 상우하좌
#             for dx, dy in zip((-1, 0, 1, 0), (0, 1, 0, -1)):
#                 nx, ny = x + dx, y + dy
#                 temp_dist = (rx - nx) ** 2 + (ry - ny) ** 2
#                 print(f'temp_dist: {temp_dist}, dist:{dist}, idx:{idx}')
#                 if in_range(nx, ny) and board[nx][ny] <= 0:
#                     if temp_dist < dist:
#                         dist = temp_dist
#                         temp_loc.append((nx, ny, dx, dy))
#
#             print(f'temp_loc - 산타 이동 {temp_loc}')
#             # 산타 이동 - temp_loc의 가장 마지막 값
#             temp_board[temp_loc[-1][0]][temp_loc[-1][1]] = idx
#             # 루돌프와 충돌
#             if (temp_loc[-1][0], temp_loc[-1][1]) == (rx, ry):
#                 # 방향 바꾸기
#                 board = collision(idx, temp_loc[-1][0], temp_loc[-1][1], -temp_loc[-1][2], -temp_loc[-1][3], d)
#                 for b in board:
#                     print(*b)
#                 print()
#                 # board[rx][ry] = -1
#                 board[temp_loc[-1][0]][temp_loc[-1][1]] = 0
#                 # 점수 획득
#                 santa[idx][0] += d
#                 # for t in temp_board:
#                 #     print(*t)
#                 print('<<산타 이동 후>>')
#                 for t in board:
#                     print(*t)
#                 print()
#                 return board
#
#
#     print('<<산타 이동 후>>')
#     for t in temp_board:
#         print(*t)
#     print()
#
#     return temp_board
#
#
#
#
# def calc():
#     pass
#
# # main
# for time in range(m):
#     # 1. 루돌프 이동
#     move_ru(time)
#
#     # 2. 산타 이동
#     board = move_santa(time)
#
#     # 3. 점수 계산
#     calc()
#
#     print('<<santa 점수>>')
#     print(*santa)
#     print()
#
# print('<<ans>>')
# for i in range(1, p):
#     print(santa[i][0], end = ' ')
# print(santa[-1][0])
#
