class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        srt = sorted((v, i) for i, v in enumerate(nums))
        val = [v for v, i in srt]
        pos = [0]*n
        for r, (v, i) in enumerate(srt):
            pos[i] = r

        hi = [0]*n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j+1 < n and val[j+1]-val[i] <= maxDiff:
                j += 1
            hi[i] = j

        comp = [0]*n
        for i in range(1, n):
            comp[i] = comp[i-1] + (val[i]-val[i-1] > maxDiff)

        LOG = max(1, n.bit_length())
        lift = [hi[:]]
        for k in range(1, LOG):
            prv = lift[-1]
            lift.append([prv[prv[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            p, q = pos[u], pos[v]
            if p > q:
                p, q = q, p
            if comp[p] != comp[q]:
                ans.append(-1)
                continue
            cur, hops = p, 0
            for k in range(LOG-1, -1, -1):
                if lift[k][cur] < q:
                    cur = lift[k][cur]
                    hops += (1 << k)
            ans.append(hops+1)
        return ans
        