class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)

        # Tree arrays
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)
        length = [0] * (4 * n)

        def build(node, l, r):
            length[node] = r - l + 1

            if l == r:
                left_char[node] = s[l]
                right_char[node] = s[l]
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node)

        def merge(node):
            left = node * 2
            right = node * 2 + 1

            left_char[node] = left_char[left]
            right_char[node] = right_char[right]

            # Start with the best answer from either side
            best[node] = max(best[left], best[right])

            prefix[node] = prefix[left]
            suffix[node] = suffix[right]

            # If the boundary characters are equal,
            # the two runs can be joined.
            if right_char[left] == left_char[right]:

                best[node] = max(
                    best[node],
                    suffix[left] + prefix[right]
                )

                # Entire left segment has the same character
                if prefix[left] == length[left]:
                    prefix[node] = length[left] + prefix[right]

                # Entire right segment has the same character
                if suffix[right] == length[right]:
                    suffix[node] = suffix[right] + suffix[left]

        def update(node, l, r, idx, char):
            if l == r:
                left_char[node] = char
                right_char[node] = char
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(best[1])

        return ans