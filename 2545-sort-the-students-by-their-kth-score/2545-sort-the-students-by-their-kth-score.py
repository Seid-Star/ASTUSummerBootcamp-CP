class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        a=len(score)
        arr=[]
        for i in range(a):
            arr.append((score[i][k],score[i]))
        arr.sort(reverse=True)
        brr=[]
        for i,j in arr:
            brr.append(j)
        return brr

