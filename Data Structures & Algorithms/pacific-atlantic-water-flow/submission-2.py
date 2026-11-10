class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows, cols = len(heights), len(heights[0])
            
        def dfs(r, c, prev, oce):
            if r < 0 or c < 0 or r == rows or c == cols:
                return
            curr = heights[r][c]
            if (r,c) in oce:
                return
            if curr >= prev:
                oce.add((r,c))
                dfs(r-1, c, curr, oce)
                dfs(r, c-1, curr, oce)
                dfs(r+1, c, curr, oce)
                dfs(r, c+1, curr, oce)
        
        for i in range(len(heights)):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, cols-1, heights[i][cols-1], atl)

        for i in range(len(heights[0])):
            dfs(0, i, heights[0][i], pac)
            dfs(rows-1, i, heights[rows-1][i], atl)
        
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                curr = (r,c)
                if curr in atl and curr in pac:
                    r, c = curr
                    res.append([r,c])
        return res
