class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols = len(heights[0])
        rows = len(heights)
        res = []

        pac = set()
        atl = set()

        for c in range(cols):
            pac.add((0,c))
            atl.add((rows-1, c))
        for r in range(rows):
            pac.add((r, 0))
            atl.add((r, cols-1))
        def dfs(r, c, visited, ocean, prev):
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited 
                or heights[r][c]<prev):
                return False
            visited.add((r,c))
            dfs(r-1, c, visited, ocean, heights[r][c])
            dfs(r+1, c, visited, ocean, heights[r][c])
            dfs(r, c-1, visited, ocean, heights[r][c])
            dfs(r, c+1, visited, ocean, heights[r][c])
            return True
        visitedatl = set()
        visitedpac = set()

        for c in range(cols):
            dfs(0, c, visitedpac, atl, heights[0][c])
            dfs(rows-1, c, visitedatl, pac, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, visitedpac, atl, heights[r][0])
            dfs(r, cols-1, visitedatl, pac, heights[r][cols-1])
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in visitedatl and (r,c) in visitedpac:
                    res.append([r,c])
                else:
                    continue
        return res
