class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        fre={}
        for i in range(len(nums)):
            if nums[i] in fre and i-fre[nums[i]]<=k:
                return True
            fre[nums[i]]=i
        return False
        