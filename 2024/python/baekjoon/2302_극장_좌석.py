import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

# dp[i]: 좌석이 i 개 일때의 경우의 수
dp = [0] * 41

# 초기화
dp[0] = 1
dp[1] = 1
dp[2] = 2

# 점화식
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2] # i-1: 좌석을 옮기지 않는 경우 / i-2: 옮기는 경우

ans = 1

# 고정석을 기준으로 경우의 수를 나누고 각 경우의 수를 곱하면 된다
# _ _ _ _ @ _ _ _ @ _ : 4칸, 3칸, 1칸의 경우의 수를 곱해준다
if m > 0:
    pre = 0 # 몇 개의 칸을 세야 하는지 기준을 잡는 것
    for j in range(m):
        ans *= dp[vip[j] - 1 - pre] # vip 사이의 좌석의 경우의 수 곱하기
        pre = vip[j]
    ans *= dp[n - pre]
else:
    ans = dp[n]

print(ans)