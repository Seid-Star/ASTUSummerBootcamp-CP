class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        E=[]
        O=[]
        for i in nums:
            if i%2==0:
                E.append(i)
            else:
                O.append(i)
        en=0
        on=0
        arr=[]
        for i in range(len(nums)):
            if i%2==0 and len(E)!=en:
                arr.append(E[en])
                en+=1
            else:
                if len(O)!=on:
                    arr.append(O[on])
                    on+=1
        return arr

        
        