class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=0
        str=''
        arr=[]
        for i in s:
            if i=='(':
                a+=1
                str+='('
            else:
                if a==1:
                    a-=1
                    str+=')'
                    arr.append(str[1:len(str)-1])
                    str=''
                else:
                    str+=')'
                    a-=1
        return ''.join(arr)

        