from typing import List
import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dist=[[-1]*n for _ in range(n)]
        q=deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dist[i][j]=0
                    q.append((i,j))

        d=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x,y=q.popleft()
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))

        heap=[(-dist[0][0],0,0)]
        vis=[[False]*n for _ in range(n)]
        vis[0][0]=True

        while heap:
            s,x,y=heapq.heappop(heap)
            s=-s
            if x==n-1 and y==n-1:
                return s
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and not vis[nx][ny]:
                    vis[nx][ny]=True
                    ns=min(s,dist[nx][ny])
                    heapq.heappush(heap,(-ns,nx,ny))