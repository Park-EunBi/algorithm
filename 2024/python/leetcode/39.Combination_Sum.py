class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        # csum: candidates sum
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                ret.append(path)
                return

            for i in range(index, len(candidates)):
                print(path)
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return ret