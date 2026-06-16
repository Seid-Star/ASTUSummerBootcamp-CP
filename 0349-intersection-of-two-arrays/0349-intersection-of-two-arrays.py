class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        l1=0
        l2=0
        arr=[]
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1]==nums2[l2]:
                arr.append(nums1[l1])
            if nums1[l1]<nums2[l2]:
                l1+=1
            else:
                l2+=1
        return arr

        