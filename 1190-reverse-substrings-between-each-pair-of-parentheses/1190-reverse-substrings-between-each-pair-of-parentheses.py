class Solution:
    def reverseParentheses(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if s[i]==')':
                b=''
                while a[-1]!='(':
                    b+=a.pop()
                a.pop()
                for j in range(len(b)):
                    a.append(b[j])
            else:
                a.append(s[i])
        return ''.join(a)