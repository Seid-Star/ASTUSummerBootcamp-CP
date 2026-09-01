class Solution:
    def minMoves(self,classroom:List[str],energy:int)->int:
        from collections import deque
        m,n=len(classroom),len(classroom[0])
        litter={}
        for r in range(m):
            for c in range(n):
                if classroom[r][c]=='S':
                    sr,sc=r,c
                elif classroom[r][c]=='L':
                    litter[(r,c)]=len(litter)
        k=len(litter)
        target=(1<<k)-1
        q=deque([(sr,sc,energy,0,0)])
        best={}
        best[(sr,sc,0)]=energy
        while q:
            r,c,e,mask,d=q.popleft()
            if mask==target:
                return d
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if not(0<=nr<m and 0<=nc<n) or classroom[nr][nc]=='X' or e==0:
                    continue
                ne=e-1
                nm=mask
                if (nr,nc) in litter:
                    nm|=1<<litter[(nr,nc)]
                if classroom[nr][nc]=='R':
                    ne=energy
                state=(nr,nc,nm)
                if ne>best.get(state,-1):
                    best[state]=ne
                    q.append((nr,nc,ne,nm,d+1))
        return -1