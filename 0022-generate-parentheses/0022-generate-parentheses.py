
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        arr = []

        def solve(s, a, b):
            if len(s) == 2*n:
                arr.append(s)
                return

            if a < n:
                solve(s + "(", a + 1, b)

            if b < a:
                solve(s + ")", a, b + 1)

        solve("", 0, 0)
        return arr
