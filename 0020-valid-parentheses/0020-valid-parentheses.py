class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i=='(':
                arr.append(')')
            elif i=='[':
                arr.append(']')
            elif i=='{':
                arr.append('}')
            else:

                if not arr or arr.pop()!=i:
                    return False
        return len(arr)==0

        