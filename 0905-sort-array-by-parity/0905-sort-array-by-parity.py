class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        E=[]
        O=[]
        for i in nums:
            if i%2==0:
                E.append(i)
            else:
                O.append(i)
        return E+O
        