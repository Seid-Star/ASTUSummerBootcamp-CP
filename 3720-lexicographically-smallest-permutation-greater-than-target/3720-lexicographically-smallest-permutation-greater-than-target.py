class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # We cannot continue matching target.
                # Backtrack and make the latest possible position larger.
                for j in range(i, -1, -1):
                    if j < i:
                        c = ord(ans[j]) - ord('a')
                        cnt[c] += 1

                    x = ord(target[j]) - ord('a')

                    # Smallest available character > target[j]
                    for c in range(x + 1, 26):
                        if cnt[c] > 0:
                            ans = ans[:j]
                            ans.append(chr(c + ord('a')))
                            cnt[c] -= 1

                            # Put remaining characters in sorted order
                            for k in range(26):
                                ans.append(chr(k + ord('a')) * cnt[k])

                            return ''.join(ans)

                return ""

        # target itself is a permutation of s.
        # Find the next lexicographical permutation.
        for j in range(len(target) - 1, -1, -1):
            c = ord(ans[j]) - ord('a')
            cnt[c] += 1

            x = ord(target[j]) - ord('a')

            for bigger in range(x + 1, 26):
                if cnt[bigger] > 0:
                    result = ans[:j]
                    result.append(chr(bigger + ord('a')))
                    cnt[bigger] -= 1

                    for k in range(26):
                        result.append(chr(k + ord('a')) * cnt[k])

                    return ''.join(result)

        return ""