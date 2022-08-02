from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 투포인터
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            # 중복일 때
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 중복이 아닐 때 투포인터
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-2,0,1,1,2]))


'''
# 브루트 포스
# Time Limit Exceeded
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums)-1):
                for k in range(j + 1, len(nums)):
                    if(nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in result):
                        result.append([nums[i], nums[j], nums[k]])
        return result
'''