# n : 볼링공의 개수
# 같은 무게의 공이더라도 다른 공으로 취급
# m: 1~m 까지 볼링공의 무게
# 둘이서 서로 다른 무게의 볼링공을 고르려고 함

# nC2 - 같은 공의 개수 (종류, 1 1 2 2 이면 2)
from itertools import combinations

n, m = map(int,input().split())
balls = list(map(int, input().split()))
balls.sort()

# 1. nC2
nums = len(list(combinations(balls, 2)))

# 2. 중복되는 종류 만큼 빼주기

# 중복 개수 세기 - hash
count = {}
for b in balls:
    if b not in count:
        count[b] = 1
    else:
        count[b] += 1

# 중복되는 종류 만큼 빼주기
for c in count:
    if count[c] != 1:
        nums -= 1

print(nums)

'''
<교재 풀이>
# 공의 개수 세기 (무게 기준)
array = [0] * 11
for b in balls:
    array[x] += 1
    
result = 0

for i in range(1, m+1):
    # 뽑을 수 있는 경우의 수가 줄어듦 
    n -= array[i]
    # 이전 계산 결과와 곱해줌
    result += array[i] * n
    
print(result)
'''


'''
<testCase>
5 3
1 3 2 3 2
<answer>
8

<testCase>
8 5
1 5 4 3 2 4 5 2
<answer>
25
'''