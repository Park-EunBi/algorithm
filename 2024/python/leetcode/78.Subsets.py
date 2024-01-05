from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        # 풀이 1
        ret = []
        for i in range(len(nums) + 1):
            ret += list(map(list, combinations(nums, i)))
        return ret
        '''

        ret = []

        def dfs(index, path):
            ret.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return ret
