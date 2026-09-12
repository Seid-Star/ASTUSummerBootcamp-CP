class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = []

        for i in range(n):
            arr.append([intervals[i][0], intervals[i][1], intervals[i][2], i])

        arr.sort()

        starts = []

        for i in range(n):
            starts.append(arr[i][0])

        next_index = [n] * n

        for i in range(n):
            l = i + 1
            r = n

            while l < r:
                mid = (l + r) // 2

                if starts[mid] > arr[i][1]:
                    r = mid
                else:
                    l = mid + 1

            next_index[i] = l

        dp = [[None] * 5 for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = (0, [])

        for k in range(5):
            dp[n][k] = (0, [])

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                skip = dp[i + 1][k]

                take_score = arr[i][2] + dp[next_index[i]][k - 1][0]

                take_indices = dp[next_index[i]][k - 1][1] + [arr[i][3]]

                take_indices.sort()

                if take_score > skip[0]:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip[0]:
                    dp[i][k] = skip

                else:
                    if take_indices < skip[1]:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = skip

        return dp[0][4][1]