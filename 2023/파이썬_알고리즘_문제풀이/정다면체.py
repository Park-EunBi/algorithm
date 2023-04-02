import sys
sys.stdin = open("input.txt", "rt")

# 정 n, m 면체 주사위를 던저 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력
# 오름차순으로 출력

n, m = map(int, input().split())

sums = [] # 합 저장
for i in range(1, n+1) :
    for j in range(1, m+1): # 중복 가능
        sums.append(i + j)

nums = set(sums) # 어떤 수가 있는지 확인
count_sum = [] # 빈도수 계산
for i in range(0, n*m + 1):
    count_sum.append(sums.count(i+1))

for i in range(0, n*m + 1):
    if count_sum[i] == max(count_sum):
        print(i+1, end=" ")

## 다른 풀이 ##
cnt = [0] * (n + m + 3)
# max = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 합을 나타내는 리스트와 수를 세는 리스트를 따로 두는 것이 아니라
        # 바로 수만 셈
        cnt[i + j] = cnt[i + j] + 1

for i in range(n + m + 1):
    if cnt[i] == max(cnt):
        print(i, end=' ')