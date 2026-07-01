class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        a=len(matrix)
        b=len(matrix[0])
        self.pre=[[0]*(b+1) for i in range(a+1)]
        for j in range(1,a+1):
            for k in range(1,b+1):
                top= self.pre[j-1][k]
                left= self.pre[j][k-1]
                overlap= self.pre[j-1][k-1]
                current=matrix[j-1][k-1]
                self.pre[j][k]=top+left-overlap+current
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a=self.pre[row2+1][col2+1]-self.pre[row1][col2+1]-self.pre[row2+1][col1]+self.pre[row1][col1]
        return a


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)