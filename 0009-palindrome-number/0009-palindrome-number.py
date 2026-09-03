class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)[::-1]
        b=str(x)
        if a==b:
            return True
        else:
            return False
        