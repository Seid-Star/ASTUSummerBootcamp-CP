class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a=len(matrix)
        b=len(matrix[0])
        arr=[]
        for i in range(b):
            arr.append([0]*a)
        for i in range(a):
            for j in range(b):
                arr[j][i]=matrix[i][j]
        return arr

        