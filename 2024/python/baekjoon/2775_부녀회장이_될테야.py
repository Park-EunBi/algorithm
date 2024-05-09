t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

    # 초기화
    dp[0] = [i for i in range(n + 1)]
    for i in range(1, k + 1):
        dp[i][1] = 1


    for i in range(1, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[k][n])