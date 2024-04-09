n, m, q = map(int, input().split())
board = [[2]*(n+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(n)]+[[2]*(n+2)]
# board = [list(map(int, input().split())) for _ in range(n)]
units = {}
init_k = [0] * (m + 1) # 초기 체력 저장
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

for m in range(1, m + 1):
    units[m] = list(map(int, input().split()))
    init_k[m] = units[m][4]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# start 번호의 기사를 dr 방향으로 밀자
def push_unit(start, dr):
    q = []
    pset = set() # 밀리는 기사 번호 저장
    damage = [0] * (m + 1) # 데미지 누적

    q.append(start) # bfs 준비
    pset.add(start) # 밀리는 기사에 저장

    while q:
        cur = q.pop(0) # 한 명 꺼냄
        ci, cj, h, w, k = units[cur]

        # 명령 받은 방향으로 이동
        # 갈 수 있으면 큐에 삽입 (벽 아닐 경우)
        ni, nj = ci + dxs[dr], cj + dys[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                # if in_range(i, j):
                    if board[i][j] == 2: # 벽이면 무시
                        return
                    if board[i][j] == 1: # 함정인 경우 데미지 누적
                        damage[cur] += 1

        # 겹치는 경우 큐에 추가 (밀릴 수 있는 경우)
        for idx in units:
            if idx in pset: continue # 이미 대상으로 체크 되어 있어 패스

            ti, tj, th, tw, tk = units[idx] # 현재 노드와 연결된 노드 확인
            # 겹치는 경우
            if ni <= ti + th - 1 and ni + h - 1 >= ti and tj <= nj + w - 1 and nj <= tj + tw - 1:
                q.append(idx)
                pset.add(idx)

    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0

    # 데미지 처리
    for idx in pset: # 밀리는 녀석이면
        si, sj, h, w, k = units[idx]

        if k <= damage[idx]: # 체력 보다 더 큰 데미지를 입음
            units.pop(idx)

        else:
            ni, nj = si + dxs[dr], sj + dys[dr] # 이동 시킨 위치 저장
            units[idx] = [ni, nj, h, w, k - damage[idx]]

# main
for _ in range(q):
    idx, dr = map(int, input().split())
    if idx in units: # 명령을 했는데 아직 기사가 살아있다면
        push_unit(idx, dr) # 기사 밀기

ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)


'''
# 0: 빈 칸, 1: 함정, 2: 벽
from collections import deque
l, n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(l)]
person = [list(map(int, input().split())) for _ in range(n)]
king = [list(map(int, input().split())) for _ in range(q)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
heart = [0 for _ in range(n + 1)] # 얼마나 다쳤는지 기록

# idx 처리
person.insert(0, []) # 명령어 처리를 위한 인덱스 처리
for i in range(1, n + 1):
    person[i][0] -= 1
    person[i][1] -= 1

print('<<inital - board>>')
for b in board:
    print(*b)
print()

def write_loc():
    for i in range(1, n + 1):
        r, c, h, w, _ = person[i]
        for x in range(r, r + h):
            for y in range(c, c + w):
                loc[x][y] = i

    print('<<위치 등록>>')
    for l in loc:
        print(*l)
    print()

def in_range(x, y):
    if x < 0 or x >= l or y < 0 or y >= l:
        return False
    return True

# i 번째 기사의 d 방향으로 누가 있는지 체크
def bfs(r, c, i, d):
    q = deque()
    q.append((r, c))
    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[r][c] = 1
    who = set()
    while q:
        x, y = q.popleft()
        print(x, y)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                # 1. 같은 수 이면 사방 확인, 확장
                # if loc[nx][ny] == i:
                if loc[nx][ny] == loc[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    who.add(loc[nx][ny]) # 이동할 사람이 누군지 확인

                # 2. 다른 수 이면 d 방향으로만 이동
                elif loc[nx][ny] == 0:
                    # 0이면 바로 탈출 - 본인만 추기
                    who.add(i)
                    # break
                    continue

                else:
                    if (dx, dy) == (dxs[d], dys[d]):
                        # d 방향으로 이동
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        who.add(loc[nx][ny]) # 이동할 사람이 누군지 확인
                    # d 방향이 아닌 곳은 무시
                    else:
                        continue

    print('<<visited - bfs>>')
    for v in visited:
        print(*v)
    print(f'who: ', *who)
    print()
    if 0 in who:
        who.remove(0)

    return who

def move(i, d):
    # i 사용 주의
    # i 번째 기사를 d 방향으로 이동
    # -> i 번째 기사의 d 방향 있는 기사들 이동
    # 해당 방향으로 누가 있는지를 알아야 함

    # 1. i 번째 기사의 d 방향으로 누가 있는지 체크
    # ! 그냥 미는 게 아니라 붙어 있어야 민다
    r, c, h, w, _ = person[i]
    # who = set()
    # 누가 붙어있는지 찾는 코드 다시 작성 -> who에 값 넣기
    # bfs로 연결된 노드 찾으면 되는데 다른 점이 방향을 정해줌
    who = bfs(r, c, i, d) # 기사의 첫 번째 위치, 기사 번호, 방향


    # for x in range(r, r + h):
    #     for y in range(c, c + w):
    #         for length in range(l):
    #             nx, ny = x + (dxs[d] * length), y + (dys[d] * length)
    #             print(f'nx, ny : {nx, ny}')
    #             # if in_range(nx, ny) and loc[nx][ny] and loc[nx][ny] != i:
    #             if in_range(nx, ny) and loc[nx][ny]:
    #                 who.add(loc[nx][ny])

    print(f'{d} 방향으로 누가 있나: {who}')

    # 2. d 방향으로 한 칸씩 밀기
    wall = False # 벽 만났는지 체크
    temp = [[0 for _ in range(l)] for _ in range(l)]
    for x in range(l):
        for y in range(l):
            if loc[x][y] in who:
                nx, ny = x + dxs[d], y + dys[d]
                # 벽인지 확인
                if in_range(nx, ny) and board[nx][ny] != 2:
                    # 이동
                    temp[nx][ny] = loc[x][y]
                else:
                    wall = True
                    break ############# 주의

            elif loc[x][y] > 0: # 밀리지 않은 부분은 그대로 복사
                temp[x][y] = loc[x][y]

    # 3. 변경된 위치 저장
    if not wall: # 변경된 부분이 있다면
        for w in who:
            person[w][0] += dxs[d]
            person[w][1] += dys[d]
            # print(w)

    print(f'벽?: {wall}')
    print('<<temp - move>>')
    for t in temp:
        print(*t)
    print()

    if wall:
        return loc, who, wall
    else:
        return temp, who, wall

# 밀린 기사들은 피해를 입음
def damage(i, who):
    print(f'who: {who} , 본인 :{i}')
    # 밀린 기사만 (본인 제외) 함정 개수 만큼 데미지
    for x in range(l):
        for y in range(l):
            # 본인을 제외한 밀린 기사라면
            if loc[x][y] in who and loc[x][y] != i:
                print(i)
                # print(loc[x][y])
                # 함정 있으면 데미지
                if board[x][y] == 1:
                    person[loc[x][y]][4] -= 1 # 체력 감소
                    print(f'누가 다친거지: {loc[x][y]}')
                    heart[loc[x][y]] += 1

    print('person - after dagame', * person)

    # 체력 다 쓴 기사는 제거
    die = [
        i
        for i in range(1, n + 1) ###
        if person[i][4] <= 0
    ]
    print(f'die 한 사람: {die}')

    for x in range(l):
        for y in range(l):
            if loc[x][y] in die:
                loc[x][y] = 0


############ 위치가 반복문 안으로 들어가야 하는지?
# 0. 기사 위치 등록
loc = [[0 for _ in range(l)] for _ in range(l)]
write_loc()
# main
for i in range(q):
    print(f'------turn {i + 1}------')
    print(king[i])

    # 1. 이동
    loc, who, wall = move(king[i][0], king[i][1])
    print('<<temp - after move>>')
    for o in loc:
        print(*o)
    print()

    # 2. 데미지 체크
    if not wall: # 이동 했을 경우에만 데미지 처리
        print(f'누굴 민건데: {king[i][0]}')
        damage(king[i][0], who) ######## 오래 걸림

# 3. 데미지 계산
print(*person)
print(*heart)
ans = 0

ans = sum([
    heart[x]
    for x in range(1, n + 1)
    if person[x][4] > 0
])

# for x in range(1, n + 1):
#     if person[x][4] > 0:
#         print(x)
#         print(f'heart: {heart[x]}')
print(ans)


# '''
# 5 5 9
# 1 0 1 1 1
# 1 1 1 1 2
# 0 1 1 0 2
# 0 1 1 0 1
# 1 1 1 1 2
# 1 2 3 2 2
# 1 4 1 2 1
# 5 1 1 2 2
# 4 5 1 1 2
# 1 1 3 1 2
# 4 2
# 2 0
# 1 2
# 4 3
# 2 0
# 5 1
# 1 2
# 2 1
# 3 2
#
# 1
# '''
#
# '''
# 4 2 100
# 2 0 0 1
# 2 1 1 2
# 0 1 0 0
# 1 1 0 0
# 3 1 1 1 7
# 4 4 1 1 3
# 2 1
# 2 2
# 1 3
# 2 1
# 2 2
# 1 1
# 1 3
# 2 0
# 1 0
# 2 2
# 1 1
# 2 0
# 2 1
# 2 1
# 1 2
# 2 0
# 1 1
# 1 0
# 1 0
# 2 0
# 1 2
# 2 3
# 2 2
# 1 2
# 1 0
# 1 1
# 2 2
# 1 1
# 2 0
# 1 1
# 1 2
# 2 0
# 1 1
# 1 1
# 2 1
# 2 0
# 2 1
# 1 2
# 2 1
# 2 0
# 2 0
# 1 0
# 1 0
# 2 3
# 2 0
# 2 2
# 2 1
# 2 1
# 1 1
# 1 3
# 2 2
# 1 3
# 1 1
# 1 0
# 1 1
# 1 3
# 1 0
# 2 0
# 2 1
# 2 1
# 2 1
# 2 2
# 1 1
# 2 2
# 1 1
# 1 1
# 1 0
# 2 3
# 1 2
# 2 3
# 1 1
# 2 2
# 2 0
# 2 0
# 1 3
# 2 3
# 1 1
# 2 3
# 2 1
# 1 3
# 1 1
# 1 3
# 1 2
# 1 3
# 1 2
# 2 3
# 1 1
# 2 1
# 1 1
# 1 0
# 1 1
# 2 1
# 2 2
# 2 1
# 1 1
# 1 0
# 1 2
# 1 1
# 2 0
# 2 0
#
# 2
# '''
#
# '''
# 10 4 4
# 2 0 0 1 1 0 2 0 1 1
# 2 1 0 0 1 0 0 0 0 0
# 0 1 1 2 1 2 1 1 1 1
# 1 2 0 2 1 0 1 1 1 0
# 1 0 0 1 0 0 1 1 0 1
# 0 2 1 0 1 1 1 0 1 1
# 1 0 2 2 1 2 2 0 0 0
# 0 1 2 0 2 2 0 1 1 0
# 0 1 1 1 1 0 1 1 0 0
# 0 0 1 0 1 2 1 1 2 0
# 7 9 3 2 20
# 9 6 1 3 15
# 3 8 1 3 10
# 4 7 3 3 5
# 3 3
# 1 0
# 4 0
# 3 2
#
# 0
# '''

