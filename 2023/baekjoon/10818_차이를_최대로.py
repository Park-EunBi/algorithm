# 가장 큰 수 - 가장 작은수
from itertools import permutations
n = int(input())
a = list(map(int, input().split(' ')))

# 걍 8개인데 다 구하자

num_lists = (permutations(a))

answer = 0
for l in num_lists:
    mid_sum = 0
    for i in range(n - 1):
        mid_sum += abs(l[i] - l[i+1])
    answer = max(mid_sum, answer)

print(answer )

'''
per = list(permutations(a))

result = -99999999
for p in per:
    tmp_result = 0
    for i in range(0, len(a)-1):
        tmp = abs(p[i] - p[i+1])
        tmp_result += tmp
    result = max(result, tmp_result)

print(result)

'''

# a_big = a.sort(reverse=True)
# a_small = a.sort(reverse=False)
# result = 0
# for i in range(n//2):
