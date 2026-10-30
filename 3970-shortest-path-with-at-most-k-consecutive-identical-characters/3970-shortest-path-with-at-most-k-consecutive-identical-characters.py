
import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        arr = [[] for i in range(n)]

        for u, v, w in edges:
            arr[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for i in range(n)]

        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, u, count = heapq.heappop(heap)

            if d > dist[u][count]:
                continue

            if u == n - 1:
                return d

            for v, w in arr[u]:
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_dist = d + w

                if new_dist < dist[v][new_count]:
                    dist[v][new_count] = new_dist
                    heapq.heappush(heap, (new_dist, v, new_count))

        return -1
