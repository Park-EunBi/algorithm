import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    files.insert(0, 0)

    # i 번째 파일 부터 j 번째 파일을 합치는 최솟값
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # 1. 초깃값
    # 두 값이 연속이면 둘을 더하기만 하면 된다
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i + 1:
                dp[i][j] = files[i] + files[j]

    # 2. 점화식
    # 맨 밑 부터 위로 올라오며 dp 채우기
    # dp[1][4]: dp[1][1] + dp[2][4], dp[1][2] + dp[3][4], dp[1][3] + dp[4][4]
    for i in range(n-1, 0, -1):
        for j in range(1, n+1):
            # dp 계산을 한 적 없고, 열>행
            if dp[i][j] == 0 and j > i:
                dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)]) + sum(files[i:j + 1])

    print(dp[1][n])
