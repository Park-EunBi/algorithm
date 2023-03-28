import sys
sys.stdin = open("input.txt", "rt")

# 내림차순 정렬
nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))
nums.sort(reverse= True)
for i in nums:
    print(i, end=' ')
