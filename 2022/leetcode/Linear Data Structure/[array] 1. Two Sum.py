from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num] = i




s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))

'''
### 브루토 포스 방식 (Brute-Force)
        for i in range(len(nums) -1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i, j]
'''

'''
### in 을 사용한 탐색 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                # nums[i+1:].index(complement) 을 사용하면 
                # num[i+1:] 으로 슬라이싱 해서 인덱스를 찾게된다 
                # 그래서 원래의 자리를 찾고 싶다면 (i+1)을 해주는 것이 좋다 
                return i, nums[i+1:].index(complement) + (i+1)
'''

'''
### 첫번째 수를 뺀 결과 키 조회
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
'''
'''
### 조회 구조 개선 
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num] = i
'''
'''
### (불가) 투포인터 방식
        # 1. 정렬이 반드시 필요 
        nums.sort()
        # 2. 그러나 정렬하면 인덱스가 엉망이 된다 
        # 값만을 구하는 문제라면 사용 가능 
        left, right = 0, len(nums)-1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
'''