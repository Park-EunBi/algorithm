import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = float('inf')
ret = [] # idx 저장

# 투 포인터
start = 0
end = n-1

while start < end:
    now = nums[start] + nums[end]

    if abs(now) < ans:
        ans = abs(now)
        ret = [start, end]

    # 0에서 멀어지면 start 이동
    if now < 0:
        start += 1
    # 0으로 가까워지면 end 이동
    else:
        end -= 1

print(nums[ret[0]], nums[ret[1]])