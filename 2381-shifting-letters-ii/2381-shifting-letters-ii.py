class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        pref=[0]*(len(s)+1)
        for l,r,d in shifts:
            if d==1:
                pref[l]+=1
                pref[r+1]-=1
            else:
                pref[l]-=1
                pref[r+1]+=1
        a=''
        b=0
        for i in range(len(s)):
            b+=pref[i]
            c=(arr.index(s[i])+b)%26
            a+=arr[c]
        return a


