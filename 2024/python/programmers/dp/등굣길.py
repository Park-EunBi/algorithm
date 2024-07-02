def solution(m, n, puddles):
    # board
    board = [[0 for _ in range(m)] for _ in range(n)]

    for p in puddles:
        if p != []:
            board[p[1] - 1][p[0] - 1] = 1

    # 1.dp 정의
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # 2. 초기화
    dp[0][0] = 1

    for i in range(n):
        if board[i][0]:
            break
        dp[i][0] = 1

    for j in range(m):
        if board[0][j]:
            break
        dp[0][j] = 1

    # 3. 점화식
    for i in range(1, n):
        for j in range(1, m):
            if not board[i][j]:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007

    return dp[n - 1][m - 1] % 1000000007