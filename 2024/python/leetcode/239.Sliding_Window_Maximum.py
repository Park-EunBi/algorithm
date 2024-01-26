class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        # sol_1 - 브루트 포스
        it not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))
        return r
        '''

        # sol_2 - 큐
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
