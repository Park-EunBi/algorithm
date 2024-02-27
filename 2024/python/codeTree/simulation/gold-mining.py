# 0: 빈 칸, 1: 금
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 어차피 격자 내부만 돌려서 범위를 확인하지 않아도 된다
# 더하는게 아니라 빼면서 마름모인지 확인하기 때문에
def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 채굴
def get_coin(k, x, y):
    c = 0 # coin
     # 모든 범위 탐색
    for a in range(n):
        for b in range(n):
            # 마름모 범위 안에 드는지 확인
            if abs(a - x) + abs(b - y) <= k:
                # 격자 내에 존재하는지 확인
                if in_range(a, b) and board[a][b]:
                    # 채굴
                    c += 1
    return c

# 채굴 비용대비 손해를 보지 않을 수 있는지 계산
def calc(k, x, y):
    # 채굴 비용
    need = k * k + (k + 1) * (k + 1)
    # 코인 획득
    coin = get_coin(k, x, y)

    if coin * m >= need: # 부등호 확인
        return coin
    return 0


# 0. k 설정
for k in range(n + 1): # n으로 설정하면 n이 짝수일 때 모든 부분을 커버할 수 없음
    # 1. 중심점 잡기
    for i in range(n):
        for j in range(n):
            ans = max(ans, calc(k, i, j))

print(ans)

'''
6 10
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1

36
'''