import sys
input = sys.stdin.readline

n = int(input())
work = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i]: i 번째 날짜에서 얻을 수 있는 최대 수익
dp = [0 for _ in range(n + 1)]

mx = 0
for i in range(n):
    mx = max(mx, dp[i])
    # 퇴사일 넘김
    if i + work[i][0] > n:
        continue

    # 해당 일을 했을 때 결과를 기록
    dp[i + work[i][0]] = max(mx + work[i][1], dp[i + work[i][0]])

print(max(dp))


'''
# 시간 초과 
work.insert(0, (0, 0)) ]

# 초기화
if work[1][0] <= n:
    dp[1] = work[1][1]

for i in range(2, n+1):
    if i + work[i][0] <= n + 1:
        for j in range(1, i):
            if work[j][0] + j <= i:
                dp[i] = max(dp[j] + work[i][1], dp[i])
    else:
        continue

print(max(dp))
'''