import sys
n = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(n):
    bigger = 0
    for k in range(i + 1, n):
        if nums[i] < nums[k]: # 조건에 안맞음, a[i] 보다 큰 수라는 것만 체크
            bigger += 1
        else: # 조건에 맞음 - 기존에 세었던 a[i] 보다 큰 값들 더해주기
            ans += bigger

print(ans)