from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 풀이 2
        # return list(combinations(list(range(1, n + 1)), k))

        # 풀이 1
        def comb(elements, start, k):
            if k == 0:
                ret.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                comb(elements, i + 1, k - 1)
                elements.pop()

        ret = []
        comb([], 1, k)
        return ret