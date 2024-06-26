def solution(number):
    n = len(number)
    cnt = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if not number[i] + number[j] + number[k]:
                    cnt += 1

    return cnt

'''
# sol2)
from itertools import combinations
def solution(number):
    cnt = 0
    
    for nums in combinations(number, 3):
        if not sum(nums):
            cnt += 1
        
    return cnt
'''