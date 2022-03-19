def solution(nums):
    animals = len(nums)//2
    nums = set(nums)
    if len(nums) < animals:
        return len(nums)
    else:
        return animals

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

'''
(다른 풀이)
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
'''