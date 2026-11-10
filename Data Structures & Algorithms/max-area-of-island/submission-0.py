class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def dfs(row, col, count):
            if row >= r or row < 0 or col >= c or col<0:
                return 0 
            if grid[row][col]==0:
                return 0 
            grid[row][col] = 0
            up = dfs(row+1, col, count)            
            down = dfs(row-1, col, count)
            left = dfs(row, col+1, count)
            right = dfs(row, col-1, count)
            count = count + up + down + left + right
            return count + 1

        area = 0
        for rows in range(len(grid)):
            for cols in range(len(grid[rows])):
                if grid[rows][cols] == 1:
                    area = max(area, dfs(rows,cols, 0))
        return area