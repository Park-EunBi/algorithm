n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

# 1. 초기화
dp[0][0] = board[0][0]
# 0행
for j in range(1, n):
    dp[0][j] = min(board[0][j], dp[0][j-1])
# 0열
for i in range(1, n):
    dp[i][0] = min(board[i][0], dp[i-1][0])

# 2. 점화식 - 동일한 상태를 어떻게 정의할지를 생각해봐야 함
for i in range(1, n):
    for j in range(1, n):
        # (해당 위치와 위, 아래에서 온 값 중 최소 값)의 최댓값
        dp[i][j] = max(min(dp[i-1][j], board[i][j]), min(dp[i][j-1], board[i][j]))
        # sol_2
        # dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), num[i][j])

print(dp[n-1][n-1])