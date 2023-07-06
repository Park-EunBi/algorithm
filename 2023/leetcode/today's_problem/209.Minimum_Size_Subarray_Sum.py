from sys import maxsize

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = maxsize
        left, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                # (i - left + 1) : length of subarray
                res = min(res, i - left + 1)
                # left를 이동시킬거니 total에서 빼주기
                total -= nums[left]
                # 포인터 이동
                left += 1

        return res if res != maxsize else 0