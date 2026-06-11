class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for i in strs:
            b=''.join(sorted(i))
            if b not in a:
                a[b]=[]
            a[b].append(i)
        return list(a.values())

        