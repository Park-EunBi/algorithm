import sys
sys.stdin = open("input.txt", "rt")

# n개의 자연수 입력 -> 각 자연수의 자릿수의 합 구하기
# 그 합이 최대인 자연수 출력
# 반드시 def digit_sum(x)을 사용하여 작성
# 합이 같은 경우 입력 순 출력

n = int(input())
nums = list(map(int, input().split()))

sums = []

def digit_sum(x):
    # 자릿수의 합을 계산
    # 125 -> 1 + 2 + 5
    res = 0
    while x >= 1:
        res += x % 10
        x = x // 10
    return res

for i in nums:
    sums.append(digit_sum(i))

print(nums[sums.index(max(sums))])