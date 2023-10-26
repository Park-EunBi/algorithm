# 배열속 원소 중 5개가 연속인 것

n = int(input())
nums = [
    int(input())
    for _ in range(n)
]

answer = 5 # answer 최대 : 4

for i in range(n):
    cnt1 = 4
    cnt2 = 4
    for j in range(n):
        if nums[i] + 5 > nums[j] and nums[i] < nums[j]:
            cnt1 -= 1
        elif nums[i] -5 < nums[j] and nums[i] > nums[j]:
            cnt2 -=1
    answer = min(answer, cnt1, cnt2)

print(answer)

'''
# 다른 풀이 
# sort 하고 작은수에서 + 5 까지 for 문 돌며 포함 여부 확인 

nums.sort()
answer = []

for i in range(0, n):
    cnt = 0
    for j in range(nums[i], nums[i] + 5):
        if j not in nums:
            cnt += 1
        answer.append(cnt)

print(min(temp))
'''