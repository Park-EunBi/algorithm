# 주어진 수를 M번 더하여 가장 큰 수 만들기
# 특정 인덱스가 연속해서 K번을 초과하여 더해질 수 없음

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse= True)

ret = 0
for i in range(1, m + 1):
    if i % k == 0:
        ret += nums[1]
    else:
        ret += nums[0]

print(ret)