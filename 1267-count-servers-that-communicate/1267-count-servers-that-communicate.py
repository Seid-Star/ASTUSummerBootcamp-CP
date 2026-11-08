class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        arr = [0] * m
        brr = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    arr[i] += 1
                    brr[j] += 1

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if arr[i] > 1 or brr[j] > 1:
                        count += 1

        return count