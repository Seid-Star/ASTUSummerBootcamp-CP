class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        a=len(grid)
        b=len(grid[0])
        count=0
        for i in range(a):
            for j in range(b):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]!=1:
                        count+=1
                    if i==a-1 or grid[i+1][j]!=1:
                        count+=1
                    if j==0 or grid[i][j-1]!=1:
                        count+=1
                    if j==b-1 or grid[i][j+1]!=1:
                        count+=1
        return count