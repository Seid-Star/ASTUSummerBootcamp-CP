class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arr=[]
            brr=[]
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in arr:
                        return False
                    arr.append(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in brr:
                        return False
                    brr.append(board[j][i])
            for x in range(0,9,3):
                for y in range(0,9,3):
                    crr=[]
                    for z in range(x,x+3):
                        for k in range(y,y+3):
                            if board[z][k]!='.':
                                if board[z][k] in crr:
                                    return False
                                crr.append(board[z][k])
        return True
        