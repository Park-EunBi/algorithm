class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        # sol_1 - 재귀
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1
        return binary_search(0, len(nums) - 1)
        '''

        '''
        # sol_2 - 반복
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
        '''

        '''
        # sol_3 - 이진 검색 모듈
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
        '''

        # sol_4 - index 사용
        try:
            return nums.index(target)
        except:
            return -1