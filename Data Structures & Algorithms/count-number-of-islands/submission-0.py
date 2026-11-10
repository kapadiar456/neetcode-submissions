class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        def dfs(r, c):
            if r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]=='0':
                return
            grid[r][c]='0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count+=1
        return count