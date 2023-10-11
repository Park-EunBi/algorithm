class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        curr_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if curr_max == float('-inf'):
                curr_max = max(window)
            elif v > curr_max:
                curr_max = v

            result.append(current_max)

            if curr_max == window.popleft():
                curr_max = float('-inf')
        return result


'''
# 시간 초과 
# 윈도우를 이동시키는 부분은 최적화가 어려움 
# => max 함수를 최적화 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            # compare_list = nums[i: i + k]
            ans.append(max(nums[i: i + k]))
        return ans 
'''

