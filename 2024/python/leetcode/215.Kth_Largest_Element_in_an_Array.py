import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        # sol_1 - heapq
        q = []
        for n in nums:
            heapq.heappush(q, -n)

        ret = 0
        for i in range(k):
            ret = heapq.heappop(q)
        return -ret
        '''

        '''
        # sol_2 - heapq.heapify
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
        '''

        '''
        # sol_3 - heapq.nlargest
        return heapq.nlargest(k, nums)[-1]
        '''

        # sol_4 - sort
        nums.sort()
        return nums[-k]