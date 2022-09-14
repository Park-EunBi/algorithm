from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        mul = 1
        for i in range(len(nums)):
            result.append(mul)
            mul *= nums[i]
        mul = 1

        for i in range(len(nums)-1, 0 -1, -1):
            # range (start, stop, step)
            # stop 은 범위 미포함이라 -1 해줘야 한다
            result[i] *= mul
            mul *= nums[i]

        return result


s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([0, 0]))
print(s.productExceptSelf([0, 4, 0]))