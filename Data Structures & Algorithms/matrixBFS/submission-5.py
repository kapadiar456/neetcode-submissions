class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def getNear(coord):
            res=[]
            r,c = coord
            ROWS = len(grid)
            COLS = len(grid[0])
            deltaRow = [1,0,-1,0]
            deltaCol = [0,1,0,-1]
            for i in range(len(deltaRow)):
                row = r + deltaRow[i]
                col = c + deltaCol[i]
                if 0<=row < ROWS and 0<=col<COLS and not grid[row][col]==1:
                    res.append((row,col))
            return res

        q = deque()
        q.append((0,0))
        visit = set()
        length=0
        while q:
            n=len(q)
            for _ in range(n):
                r,c = q.popleft()
                if r==len(grid)-1 and c ==len(grid[0])-1:
                    return length
                visit.add((r,c))
                for near in getNear((r,c)):
                    if near in visit:
                        continue
                    q.append(near) 
            length+=1
        if grid[0][0]==1:
            return -1
        return length
                       
