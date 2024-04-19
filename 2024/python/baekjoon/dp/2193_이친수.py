n = int(input())

# dp[i][0]: i자리 이친수 중 끝의 자리가 0인 수의 개수
# dp[i][1]: i자리 이친수 중 끝의 자리가 1인 수의 개수
dp = [[0, 0] for _ in range(100)] # 안전하게 최대 수로 만들기

# 초기화
dp[0] = [0, 1]
# dp[1] = [1, 1] # 초기화 주의... 11도 안된다 10만 가능

# 점화식
# dp[i][0] = dp[i-1][1] + dp[i-1][0]
# dp[i][1] = dp[i-1][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n-1]))