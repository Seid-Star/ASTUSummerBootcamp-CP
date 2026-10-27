class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[nums2[0]]
        arr=[-1]*len(nums1)
        for i in range(1,len(nums2)):
            while len(stack)>0 and stack[-1]<nums2[i]:
                # hos=  stack.pop()
                if stack[-1] in nums1:
                    arr[nums1.index(stack[-1])]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return arr
        