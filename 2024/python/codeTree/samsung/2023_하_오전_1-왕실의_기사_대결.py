# 0: 빈 칸, 1: 함정, 2: 벽
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


def move(i, d):
    # i 사용 주의
    # i 번째 기사를 d 방향으로 이동
    # -> i 번째 기사의 d 방향 있는 기사들 이동
    # 해당 방향으로 누가 있는지를 알아야 함

    # 1. i 번째 기사의 d 방향으로 누가 있는지 체크
    # ! 그냥 미는 게 아니라 붙어 있어야 민다
    r, c, h, w, _ = person[i]
    who = set()
    for x in range(r, r + h):
        for y in range(c, c + w):
            for length in range(l):
                nx, ny = x + (dxs[d] * length), y + (dys[d] * length)
                # if in_range(nx, ny) and loc[nx][ny] and loc[nx][ny] != i:
                if in_range(nx, ny) and loc[nx][ny]:
                    who.add(loc[nx][ny])

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
        for i in range(1, n)
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


'''
5 5 9
1 0 1 1 1
1 1 1 1 2
0 1 1 0 2
0 1 1 0 1
1 1 1 1 2
1 2 3 2 2
1 4 1 2 1
5 1 1 2 2
4 5 1 1 2
1 1 3 1 2
4 2
2 0
1 2
4 3
2 0
5 1
1 2
2 1
3 2

1
'''