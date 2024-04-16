n = int(input())
# 1. 테이블 정의하기 - d[i] 를 1로 만들기 위해 필요한 최소 연산 수
dp = [0] * (n + 1)

# 2. 점화식 찾기
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])

    # 2와 3으로 나누어 질 수 있는 경우
    # 2로 나누었을 때의 값이 최소가 됨을 보장할 수 없다 -> elif 불가
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])