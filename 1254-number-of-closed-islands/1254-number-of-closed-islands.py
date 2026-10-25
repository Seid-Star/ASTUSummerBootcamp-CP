
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(a, b):
            if a < 0 or a >= m or b < 0 or b >= n:
                return

            if grid[a][b] == 1:
                return

            grid[a][b] = 1

            dfs(a + 1, b)
            dfs(a - 1, b)
            dfs(a, b + 1)
            dfs(a, b - 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        count = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)

        return count
