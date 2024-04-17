n = int(input())

# dp[i]: i를 1로 만드는 연산의 최소 횟수
dp = [0 for _ in range(n + 1)]
dp.append(0)
dp.append(0)

# 경로 복원 테이블
route = [0 for _ in range(n + 1)]
route.append(0)
route.append(0)

# 초기화
dp[1] = 0

# 점화식
for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    route[i] = i-1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        route[i] = i//3

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        route[i] = i//2


print(dp[n])

idx = n
while 1:
    print(idx, end = ' ')
    if idx == 1:
        break
    idx = route[idx]

