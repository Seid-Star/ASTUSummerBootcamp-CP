class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i in range(len(s)):
            x = ord(s[i]) - ord('a')

            if first[x] == len(s):
                first[x] = i

            last[x] = i

        arr = []

        for i in range(26):
            if first[i] == len(s):
                continue

            l = first[i]
            r = last[i]
            ok = True

            j = l

            while j <= r:
                x = ord(s[j]) - ord('a')

                if first[x] < l:
                    ok = False
                    break

                if last[x] > r:
                    r = last[x]

                j += 1

            if ok:
                arr.append([l, r])

        arr.sort(key=lambda x: x[1])

        ans = []
        last_end = -1

        for l, r in arr:
            if l > last_end:
                ans.append(s[l:r + 1])
                last_end = r

        return ans
