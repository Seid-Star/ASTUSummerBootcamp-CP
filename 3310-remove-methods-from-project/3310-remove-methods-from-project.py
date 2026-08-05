from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        vis = [False] * n

        def dfs(node):
            vis[node] = True
            for nxt in graph[node]:
                if not vis[nxt]:
                    dfs(nxt)

        dfs(k)

        for u, v in invocations:
            if not vis[u] and vis[v]:
                return list(range(n))

        ans = []

        for i in range(n):
            if not vis[i]:
                ans.append(i)

        return ans