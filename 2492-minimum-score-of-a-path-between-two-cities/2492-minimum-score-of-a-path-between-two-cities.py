from typing import List
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b, w in roads:
            g[a].append((b, w))
            g[b].append((a, w))
        vis = [False] * (n + 1)
        ans = float('inf')
        def dfs(u):
            nonlocal ans
            vis[u] = True
            for v, w in g[u]:
                ans = min(ans, w)
                if not vis[v]:
                    dfs(v)
        dfs(1)
        return ans