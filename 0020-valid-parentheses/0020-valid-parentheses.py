class Solution:
    def isValid(self, s: str) -> bool:
        b = []
        for i in s:
            if i == '(':
                b.append('(')     
            elif i == ')':
                if len(b) == 0:
                    return False
                if b[-1] != '(':
                    return False
                b.pop()       
            elif i == '{':
                b.append('{') 
            elif i == '}':
                if len(b) == 0:
                    return False
                if b[-1] != '{':
                    return False
                b.pop()  
            elif i == '[':
                b.append('[')
            
            elif i == ']':
                if len(b) == 0:
                    return False
                if b[-1] != '[':
                    return False
                b.pop()
        if len(b) == 0:
            return True 
        return False