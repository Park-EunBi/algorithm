from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 풀이 2
        # return list(permutations(nums, len(nums)))

        # 풀이 1
        result = []
        picked = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(picked[:])
                return

            for e in elements:
                unpicked = elements[:]
                unpicked.remove(e)

                picked.append(e)
                dfs(unpicked)
                picked.pop()

        dfs(nums)
        return result