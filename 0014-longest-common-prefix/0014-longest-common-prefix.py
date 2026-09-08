class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        a=strs[0]
        b=''
        for i in range(len(a)):
            b=strs[0][i]
            for x in strs[1:]:
                if i>=len(x) or x[i]!=b:
                    return strs[0][:i]
        return strs[0]                  


        