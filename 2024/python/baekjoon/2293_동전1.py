import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i]: i를 만들 수 있는 최대 경우의 수
dp = [0] * (k + 1)

# 초기화
dp[0] = 1

# 점화식 - 이전까지 만든 값에 해당 숫자로 만들 수 있는 개수를 추가
for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])