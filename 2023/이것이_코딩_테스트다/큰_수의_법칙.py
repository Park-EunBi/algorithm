import sys
sys.stdin = open("input.txt", "rt")

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# n: 배열의 크기
# m: 더해지는 횟수
# k: 최대 반복 횟수

nums.sort(reverse= True)

'''
# 일반적인 풀이
res = 0
while m > 0:
    for i in range(k):
        res += nums[0]
        m -= 1
    res += nums[1]
    m -= 1

print(res)
'''

# 시간 줄이는 풀이
# m = 8, k = 3이고, 가장 큰 수가 6, 다음 수가 5 이라면
# {6, 6, 6, 5}를 하나의 덩어리로 볼 수 있다
# 이게 몇번 반복 되는지를 이용한 풀이

res = 0
# 가장 큰 수가 더해지는 횟수
count = int(m/ (k + 1)) * k # 한 덩이가 총 몇번 반복 되는 지 * 최대 반복 횟수
count_res = m % (k +1) # 한 바퀴를 다 돌지 못하고 남은 횟수

res += ((count + count_res) * nums[0])
res += ((m - count)* nums[1])
print(res)