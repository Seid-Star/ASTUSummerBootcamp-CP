class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        k = k % (m * n)
        arr = arr[-k:] + arr[:-k]
        ans = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            ans.append(row)

        return ans