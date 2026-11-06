class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        arr = sorted((q, i) for i, q in enumerate(queries))

        brr = [0] * (n + 1)
        ans = [0] * len(queries)

        left = 0
        right = 0
        count = 0

        for q, i in arr:

            while right < len(logs) and logs[right][1] <= q:
                a = logs[right][0]

                if brr[a] == 0:
                    count += 1

                brr[a] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                a = logs[left][0]

                brr[a] -= 1

                if brr[a] == 0:
                    count -= 1

                left += 1

            ans[i] = n - count

        return ans