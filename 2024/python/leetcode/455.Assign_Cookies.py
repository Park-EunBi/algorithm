class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sol_1 - 그리디
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
        return child_i

        '''        
        # sol_2 - 이진 검색
        g.sort()
        s.sort()

        ret = 0
        for i in s:
            # 이진 검색
            index = bisect.bisect_right(g, i)
            if index > ret:
                ret += 1
        return ret
        '''