# 작은 두 수 꺼내서 더하고 다시 넣고
# 원소가 1개가 될 때 까지

import heapq

n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

'''
# heap 사용할 거면 heqp으로 만들어 줘야 한다 
# 일반 리스트로 받으면 안된다 
nums = [
    int(input())
    for _ in range(n)
]
'''

ret = 0

while len(nums) > 1:
    # 작은 두 수 꺼내기
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    ret += (a + b)
    heapq.heappush(nums, a + b)

print(ret)