class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            # 예외처리
            if x < 0 or x >= n or y < 0 or y >= m:
                return False

            # '0', '1'은 문자임
            if grid[x][y] == '1':
                self.cnt += 1
                grid[x][y] = '0'
                # 상하좌우 재귀
                dfs(x + 1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)
                return True
            return False

        n = len(grid)
        m = len(grid[0])
        ret = []
        self.cnt = 0

        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    ret.append(self.cnt)
                    self.cnt = 0

        return len(ret)