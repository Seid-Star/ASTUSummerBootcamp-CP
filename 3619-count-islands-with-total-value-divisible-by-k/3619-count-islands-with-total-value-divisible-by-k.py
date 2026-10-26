
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0
                    grid[i][j] = -grid[i][j]

                    while stack:
                        x, y = stack.pop()
                        total -= grid[x][y]

                        for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            c = x + a
                            d = y + b

                            if 0 <= c < m and 0 <= d < n and grid[c][d] > 0:
                                stack.append((c, d))
                                grid[c][d] = -grid[c][d]

                    if total % k == 0:
                        count += 1

        return count
