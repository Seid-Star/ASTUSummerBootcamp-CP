
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        mod = 10**9 + 7

        arr = [[0] * b for i in range(a)]
        brr = [[0] * b for i in range(a)]

        for i in range(a):
            for j in range(b):

                if i == 0 and j == 0:
                    count = 1
                else:
                    count = (arr[i][j] + brr[i][j]) % mod

                if i == a - 1 and j == b - 1:
                    return count

                if grid[i][j] == 1:

                    if i + 1 < a:
                        brr[i + 1][j] += arr[i][j]
                        brr[i + 1][j] %= mod

                    if j + 1 < b:
                        arr[i][j + 1] += brr[i][j]
                        arr[i][j + 1] %= mod

                else:

                    if j + 1 < b:
                        arr[i][j + 1] += count
                        arr[i][j + 1] %= mod

                    if i + 1 < a:
                        brr[i + 1][j] += count
                        brr[i + 1][j] %= mod

        return 0
