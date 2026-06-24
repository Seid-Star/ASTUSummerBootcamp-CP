class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        count=0
        while r<len(s):
            if len(set(s[l:r+1]))==len(s[l:r+1]):
                count=max(count,r-l+1)
                r+=1
            else:
                l+=1
        return count
        