class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        a=len(colors)
        count=0
        if colors[0]==colors[a-2] and colors[0]!=colors[a-1]:
            count+=1
        if colors[1]==colors[a-1] and colors[0]!=colors[1]:
            count+=1
        for i in range(1, a - 1):
            if colors[i - 1] == colors[i + 1] and colors[i - 1] != colors[i]:
                count += 1

        return count
        
        