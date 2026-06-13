from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26
            # reverse mapping: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            res.append(chr(ord('z') - rem))

        return "".join(res)