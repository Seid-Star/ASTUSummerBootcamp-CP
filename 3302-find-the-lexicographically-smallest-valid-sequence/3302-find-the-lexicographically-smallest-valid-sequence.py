from typing import List
from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        pos = [[] for _ in range(26)]
        for i, c in enumerate(word1):
            pos[ord(c) - 97].append(i)

        exact = [-1] * (m + 1)
        exact[m] = n

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                exact[j] = i
                j -= 1

        if exact[0] == -1:
            pass

        run_start = [0] * n
        for i in range(1, n):
            if word1[i] == word1[i - 1]:
                run_start[i] = run_start[i - 1]
            else:
                run_start[i] = i

        one = [-1] * (m + 1)
        one[m] = n

        for j in range(m - 1, -1, -1):
            target = ord(word2[j]) - 97

            bound = one[j + 1]
            arr = pos[target]
            k = bisect_left(arr, bound) - 1
            same = arr[k] if k >= 0 else -1

            bound = exact[j + 1]
            different = -1

            if bound > 0:
                i = bound - 1
                if word1[i] != word2[j]:
                    different = i
                else:
                    different = run_start[i] - 1

            one[j] = max(same, different)

        ans = []
        j = 0
        changed = False
        start = 0

        while j < m:
            target = word2[j]

            for i in range(start, n):
                if word1[i] == target:
                    if one[j + 1] > i:
                        ans.append(i)
                        start = i + 1
                        j += 1
                        break
                elif not changed:
                    if exact[j + 1] > i:
                        ans.append(i)
                        start = i + 1
                        j += 1
                        changed = True
                        break
            else:
                return []

        return ans