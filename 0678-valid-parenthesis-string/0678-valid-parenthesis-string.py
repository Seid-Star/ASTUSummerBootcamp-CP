class Solution:
    def checkValidString(self, s: str) -> bool:
        a = 0
        b = 0

        for i in range(len(s)):
            if s[i] == '(':
                a += 1
                b += 1

            elif s[i] == ')':
                a -= 1
                b -= 1

            else:
                a -= 1
                b += 1

            if b < 0:
                return False

            if a < 0:
                a = 0

        return a == 0